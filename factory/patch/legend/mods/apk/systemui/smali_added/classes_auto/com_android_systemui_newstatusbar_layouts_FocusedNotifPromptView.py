"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/FocusedNotifPromptView.smali'
CLASS_FALLBACK_NAMES = ['FocusedNotifPromptView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;
.super Lcom/android/systemui/statusbar/phone/FocusedNotifPromptView;


# instance fields
.field private final margin:I


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 4

    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/phone/FocusedNotifPromptView;-><init>(Landroid/content/Context;)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "focused_notif_content_start"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->getDimen(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->margin:I

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 5

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/phone/FocusedNotifPromptView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "focused_notif_content_start"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->getDimen(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->margin:I

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 6

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/phone/FocusedNotifPromptView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "focused_notif_content_start"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->getDimen(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->margin:I

    return-void
.end method


# virtual methods
.method protected onLayout(ZIIII)V
    .registers 14

    goto/32 :goto_92

    nop

    :goto_4
    invoke-virtual {v6}, Lcom/android/systemui/statusbar/phone/FocusedNotifPromptImageView;->getMeasuredHeight()I

    move-result v6

    goto/32 :goto_5e

    nop

    :goto_c
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->getMeasuredHeight()I

    move-result v0

    goto/32 :goto_b3

    nop

    :goto_14
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->mContent:Landroid/widget/FrameLayout;

    goto/32 :goto_c6

    nop

    :goto_1a
    iget-object v7, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->mContent:Landroid/widget/FrameLayout;

    goto/32 :goto_83

    nop

    :goto_20
    if-eqz v0, :cond_25

    goto/32 :goto_e4

    :cond_25
    goto/32 :goto_e2

    nop

    :goto_29
    div-int/lit8 v4, v4, 0x2

    goto/32 :goto_51

    nop

    :goto_2f
    return-void

    :goto_30
    goto/32 :goto_e8

    nop

    :goto_34
    iget-object v6, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->mIcon:Lcom/android/systemui/statusbar/phone/FocusedNotifPromptImageView;

    goto/32 :goto_4

    nop

    :goto_3a
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->mIcon:Lcom/android/systemui/statusbar/phone/FocusedNotifPromptImageView;

    goto/32 :goto_40

    nop

    :goto_40
    const/4 v3, 0x0

    goto/32 :goto_70

    nop

    :goto_45
    sub-int v4, v0, v4

    goto/32 :goto_6a

    nop

    :goto_4b
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->mContent:Landroid/widget/FrameLayout;

    goto/32 :goto_20

    nop

    :goto_51
    move v5, v4

    goto/32 :goto_a4

    nop

    :goto_56
    invoke-virtual {v1}, Lcom/android/systemui/statusbar/phone/FocusedNotifPromptImageView;->getMeasuredWidth()I

    move-result v1

    goto/32 :goto_3a

    nop

    :goto_5e
    add-int/2addr v6, v5

    goto/32 :goto_8b

    nop

    :goto_63
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->mContent:Landroid/widget/FrameLayout;

    goto/32 :goto_7b

    nop

    :goto_69
    return-void

    :goto_6a
    div-int/lit8 v4, v4, 0x2

    goto/32 :goto_dd

    nop

    :goto_70
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->mIcon:Lcom/android/systemui/statusbar/phone/FocusedNotifPromptImageView;

    goto/32 :goto_b9

    nop

    :goto_76
    add-int/2addr v3, v1

    goto/32 :goto_63

    nop

    :goto_7b
    invoke-virtual {v4}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v4

    goto/32 :goto_cc

    nop

    :goto_83
    invoke-virtual {v7}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v7

    goto/32 :goto_c1

    nop

    :goto_8b
    invoke-virtual {v2, v3, v4, v1, v6}, Lcom/android/systemui/statusbar/phone/FocusedNotifPromptImageView;->layout(IIII)V

    goto/32 :goto_14

    nop

    :goto_92
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->mIcon:Lcom/android/systemui/statusbar/phone/FocusedNotifPromptImageView;

    goto/32 :goto_aa

    nop

    :goto_98
    add-int/2addr v6, v1

    goto/32 :goto_d2

    nop

    :goto_9d
    invoke-virtual {v2, v3, v4, v6, v7}, Landroid/widget/FrameLayout;->layout(IIII)V

    goto/32 :goto_2f

    nop

    :goto_a4
    iget v6, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->margin:I

    goto/32 :goto_98

    nop

    :goto_aa
    if-nez v0, :cond_af

    goto/32 :goto_30

    :cond_af
    goto/32 :goto_4b

    nop

    :goto_b3
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->mIcon:Lcom/android/systemui/statusbar/phone/FocusedNotifPromptImageView;

    goto/32 :goto_56

    nop

    :goto_b9
    invoke-virtual {v4}, Lcom/android/systemui/statusbar/phone/FocusedNotifPromptImageView;->getMeasuredHeight()I

    move-result v4

    goto/32 :goto_45

    nop

    :goto_c1
    add-int/2addr v7, v5

    goto/32 :goto_9d

    nop

    :goto_c6
    iget v3, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->margin:I

    goto/32 :goto_76

    nop

    :goto_cc
    sub-int v4, v0, v4

    goto/32 :goto_29

    nop

    :goto_d2
    iget-object v7, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->mContent:Landroid/widget/FrameLayout;

    goto/32 :goto_ef

    nop

    :goto_d8
    add-int/2addr v6, v7

    goto/32 :goto_1a

    nop

    :goto_dd
    move v5, v4

    goto/32 :goto_34

    nop

    :goto_e2
    goto/16 :goto_30

    :goto_e4
    goto/32 :goto_c

    nop

    :goto_e8
    invoke-super/range {p0 .. p5}, Lcom/android/systemui/statusbar/phone/FocusedNotifPromptView;->onLayout(ZIIII)V

    goto/32 :goto_69

    nop

    :goto_ef
    invoke-virtual {v7}, Landroid/widget/FrameLayout;->getMeasuredWidth()I

    move-result v7

    goto/32 :goto_d8

    nop
.end method

.method protected onMeasure(II)V
    .registers 5

    goto/32 :goto_6c

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->mContent:Landroid/widget/FrameLayout;

    goto/32 :goto_44

    nop

    :goto_a
    add-int/2addr v0, v1

    goto/32 :goto_87

    nop

    :goto_f
    invoke-virtual {p0, v0, v1}, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->setMeasuredDimension(II)V

    goto/32 :goto_5e

    nop

    :goto_16
    invoke-virtual {p0, v0, v1}, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->setMeasuredDimension(II)V

    :goto_19
    goto/32 :goto_73

    nop

    :goto_1d
    invoke-virtual {v0}, Lcom/android/systemui/statusbar/phone/FocusedNotifPromptImageView;->getMeasuredWidth()I

    move-result v0

    goto/32 :goto_25

    nop

    :goto_25
    iget v1, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->margin:I

    goto/32 :goto_a

    nop

    :goto_2b
    invoke-virtual {v0}, Lcom/android/systemui/statusbar/phone/FocusedNotifPromptImageView;->getVisibility()I

    move-result v0

    goto/32 :goto_8d

    nop

    :goto_33
    if-eqz v0, :cond_38

    goto/32 :goto_5f

    :cond_38
    :goto_38
    goto/32 :goto_81

    nop

    :goto_3c
    invoke-virtual {v0}, Landroid/widget/FrameLayout;->getVisibility()I

    move-result v0

    goto/32 :goto_33

    nop

    :goto_44
    if-nez v0, :cond_49

    goto/32 :goto_5f

    :cond_49
    goto/32 :goto_96

    nop

    :goto_4d
    invoke-virtual {v1}, Landroid/widget/FrameLayout;->getMeasuredWidth()I

    move-result v1

    goto/32 :goto_b2

    nop

    :goto_55
    if-eqz v0, :cond_5a

    goto/32 :goto_5f

    :cond_5a
    goto/32 :goto_b7

    nop

    :goto_5e
    goto :goto_19

    :goto_5f
    goto/32 :goto_7c

    nop

    :goto_63
    if-nez v0, :cond_68

    goto/32 :goto_5f

    :cond_68
    goto/32 :goto_4

    nop

    :goto_6c
    invoke-super {p0, p1, p2}, Lcom/android/systemui/statusbar/phone/FocusedNotifPromptView;->onMeasure(II)V

    goto/32 :goto_aa

    nop

    :goto_73
    return-void

    :goto_74
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->getMeasuredHeight()I

    move-result v1

    goto/32 :goto_16

    nop

    :goto_7c
    const/4 v0, 0x0

    goto/32 :goto_74

    nop

    :goto_81
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->mIcon:Lcom/android/systemui/statusbar/phone/FocusedNotifPromptImageView;

    goto/32 :goto_1d

    nop

    :goto_87
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->mContent:Landroid/widget/FrameLayout;

    goto/32 :goto_4d

    nop

    :goto_8d
    if-nez v0, :cond_92

    goto/32 :goto_38

    :cond_92
    goto/32 :goto_9c

    nop

    :goto_96
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->mIcon:Lcom/android/systemui/statusbar/phone/FocusedNotifPromptImageView;

    goto/32 :goto_2b

    nop

    :goto_9c
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->mContent:Landroid/widget/FrameLayout;

    goto/32 :goto_3c

    nop

    :goto_a2
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->getMeasuredHeight()I

    move-result v1

    goto/32 :goto_f

    nop

    :goto_aa
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->getVisibility()I

    move-result v0

    goto/32 :goto_55

    nop

    :goto_b2
    add-int/2addr v0, v1

    goto/32 :goto_a2

    nop

    :goto_b7
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/FocusedNotifPromptView;->mIcon:Lcom/android/systemui/statusbar/phone/FocusedNotifPromptImageView;

    goto/32 :goto_63

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_FocusedNotifPromptView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
