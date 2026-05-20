"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/InOutView.smali'
CLASS_FALLBACK_NAMES = ['InOutView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/views/InOutView;
.super Landroid/widget/FrameLayout;


# instance fields
.field private inOutChild:Landroid/view/View;

.field private mainChild:Landroid/view/View;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Landroid/widget/FrameLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method


# virtual methods
.method protected onFinishInflate()V
    .registers 2

    goto/32 :goto_2b

    nop

    :goto_4
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/InOutView;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_c

    nop

    :goto_c
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/InOutView;->mainChild:Landroid/view/View;

    goto/32 :goto_13

    nop

    :goto_12
    return-void

    :goto_13
    const/4 v0, 0x1

    goto/32 :goto_1e

    nop

    :goto_18
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/InOutView;->inOutChild:Landroid/view/View;

    goto/32 :goto_12

    nop

    :goto_1e
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/InOutView;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_18

    nop

    :goto_26
    const/4 v0, 0x0

    goto/32 :goto_4

    nop

    :goto_2b
    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    goto/32 :goto_26

    nop
.end method

.method protected onLayout(ZIIII)V
    .registers 11

    goto/32 :goto_85

    nop

    :goto_4
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/InOutView;->mainChild:Landroid/view/View;

    goto/32 :goto_8b

    nop

    :goto_a
    invoke-virtual {v4}, Landroid/view/View;->getMeasuredHeight()I

    move-result v4

    goto/32 :goto_4c

    nop

    :goto_12
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/views/InOutView;->inOutChild:Landroid/view/View;

    goto/32 :goto_a

    nop

    :goto_18
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/InOutView;->mainChild:Landroid/view/View;

    goto/32 :goto_3c

    nop

    :goto_1e
    invoke-virtual {v0}, Landroid/view/View;->getMeasuredWidth()I

    move-result v0

    goto/32 :goto_4

    nop

    :goto_26
    sub-int v3, v0, v3

    goto/32 :goto_12

    nop

    :goto_2c
    return-void

    :goto_2d
    invoke-virtual {v0}, Landroid/view/View;->getMeasuredWidth()I

    move-result v0

    goto/32 :goto_77

    nop

    :goto_35
    invoke-virtual {v2, v3, v3, v0, v1}, Landroid/view/View;->layout(IIII)V

    goto/32 :goto_71

    nop

    :goto_3c
    invoke-virtual {v0}, Landroid/view/View;->getVisibility()I

    move-result v0

    goto/32 :goto_5f

    nop

    :goto_44
    invoke-virtual {v2}, Landroid/view/View;->getMeasuredWidth()I

    move-result v3

    goto/32 :goto_26

    nop

    :goto_4c
    sub-int v4, v1, v4

    goto/32 :goto_58

    nop

    :goto_52
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/InOutView;->mainChild:Landroid/view/View;

    goto/32 :goto_1e

    nop

    :goto_58
    invoke-virtual {v2, v3, v4, v0, v1}, Landroid/view/View;->layout(IIII)V

    :goto_5b
    goto/32 :goto_2c

    nop

    :goto_5f
    if-eqz v0, :cond_64

    goto/32 :goto_5b

    :cond_64
    goto/32 :goto_52

    nop

    :goto_68
    if-nez v0, :cond_6d

    goto/32 :goto_5b

    :cond_6d
    goto/32 :goto_2d

    nop

    :goto_71
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/views/InOutView;->inOutChild:Landroid/view/View;

    goto/32 :goto_44

    nop

    :goto_77
    if-gtz v0, :cond_7c

    goto/32 :goto_5b

    :cond_7c
    goto/32 :goto_18

    nop

    :goto_80
    const/4 v3, 0x0

    goto/32 :goto_35

    nop

    :goto_85
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/InOutView;->mainChild:Landroid/view/View;

    goto/32 :goto_68

    nop

    :goto_8b
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    goto/32 :goto_93

    nop

    :goto_93
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/views/InOutView;->mainChild:Landroid/view/View;

    goto/32 :goto_80

    nop
.end method

.method protected onMeasure(II)V
    .registers 6

    goto/32 :goto_c

    nop

    :goto_4
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/InOutView;->getAlpha()F

    move-result v0

    goto/32 :goto_21

    nop

    :goto_c
    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V

    goto/32 :goto_a2

    nop

    :goto_13
    const/4 v1, 0x0

    goto/32 :goto_7c

    nop

    :goto_18
    if-eqz v0, :cond_1d

    goto/32 :goto_46

    :cond_1d
    goto/32 :goto_4a

    nop

    :goto_21
    const/4 v2, 0x0

    goto/32 :goto_56

    nop

    :goto_26
    invoke-virtual {p0, v1, v1}, Lcom/android/systemui/newstatusbar/views/InOutView;->setMeasuredDimension(II)V

    goto/32 :goto_85

    nop

    :goto_2d
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    goto/32 :goto_35

    nop

    :goto_35
    invoke-virtual {p0, v0, v1}, Lcom/android/systemui/newstatusbar/views/InOutView;->setMeasuredDimension(II)V

    goto/32 :goto_45

    nop

    :goto_3c
    if-nez v0, :cond_41

    goto/32 :goto_46

    :cond_41
    goto/32 :goto_50

    nop

    :goto_45
    goto :goto_5f

    :goto_46
    goto/32 :goto_5c

    nop

    :goto_4a
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/InOutView;->mainChild:Landroid/view/View;

    goto/32 :goto_6c

    nop

    :goto_50
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/InOutView;->mainChild:Landroid/view/View;

    goto/32 :goto_63

    nop

    :goto_56
    cmpl-float v0, v0, v2

    goto/32 :goto_3c

    nop

    :goto_5c
    invoke-virtual {p0, v1, v1}, Lcom/android/systemui/newstatusbar/views/InOutView;->setMeasuredDimension(II)V

    :goto_5f
    goto/32 :goto_92

    nop

    :goto_63
    if-nez v0, :cond_68

    goto/32 :goto_46

    :cond_68
    goto/32 :goto_74

    nop

    :goto_6c
    invoke-virtual {v0}, Landroid/view/View;->getMeasuredWidth()I

    move-result v0

    goto/32 :goto_aa

    nop

    :goto_74
    invoke-virtual {v0}, Landroid/view/View;->getWidth()I

    move-result v0

    goto/32 :goto_93

    nop

    :goto_7c
    if-nez v0, :cond_81

    goto/32 :goto_86

    :cond_81
    goto/32 :goto_26

    nop

    :goto_85
    return-void

    :goto_86
    goto/32 :goto_4

    nop

    :goto_8a
    invoke-virtual {v0}, Landroid/view/View;->getVisibility()I

    move-result v0

    goto/32 :goto_18

    nop

    :goto_92
    return-void

    :goto_93
    if-gtz v0, :cond_98

    goto/32 :goto_46

    :cond_98
    goto/32 :goto_9c

    nop

    :goto_9c
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/InOutView;->mainChild:Landroid/view/View;

    goto/32 :goto_8a

    nop

    :goto_a2
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/InOutView;->getVisibility()I

    move-result v0

    goto/32 :goto_13

    nop

    :goto_aa
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/InOutView;->mainChild:Landroid/view/View;

    goto/32 :goto_2d

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_InOutView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
