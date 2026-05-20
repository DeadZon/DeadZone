"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer.smali'
CLASS_FALLBACK_NAMES = ['MiuiNotificationStatusContainer.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;
.super Lcom/android/systemui/statusbar/views/MiuiNotificationStatusContainer;


# instance fields
.field private ids:I


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiNotificationStatusContainer;-><init>(Landroid/content/Context;)V

    const/4 v0, 0x0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->ids:I

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/views/MiuiNotificationStatusContainer;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const/4 v0, 0x0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->ids:I

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/views/MiuiNotificationStatusContainer;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const/4 v0, 0x0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->ids:I

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V
    .registers 6

    invoke-direct {p0, p1, p2, p3, p4}, Lcom/android/systemui/statusbar/views/MiuiNotificationStatusContainer;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    const/4 v0, 0x0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->ids:I

    return-void
.end method

.method private getPrivacyContainerMarginStart()I
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mPrivacyContainer:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup$MarginLayoutParams;

    invoke-virtual {v0}, Landroid/view/ViewGroup$MarginLayoutParams;->getMarginStart()I

    move-result v0

    return v0
.end method


# virtual methods
.method public final onMeasure(II)V
    .registers 20

    move-object/from16 v6, p0

    invoke-static/range {p1 .. p1}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result v7

    invoke-static/range {p2 .. p2}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result v8

    invoke-static/range {p1 .. p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v9

    invoke-static/range {p2 .. p2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v10

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mPrivacyContainer:Landroid/view/View;

    if-eqz v0, :cond_30

    iget v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->ids:I

    if-nez v0, :cond_26

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "privacy_dot_image"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    iput v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->ids:I

    :cond_26
    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mPrivacyContainer:Landroid/view/View;

    iget v1, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->ids:I

    invoke-virtual {v0, v1}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    iput-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mDotView:Landroid/view/View;

    :cond_30
    const/4 v11, 0x0

    const/4 v12, 0x0

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mDotView:Landroid/view/View;

    const/16 v13, 0x8

    if-eqz v0, :cond_64

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mDotView:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->getVisibility()I

    move-result v0

    if-eq v0, v13, :cond_64

    iget-object v1, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mPrivacyContainer:Landroid/view/View;

    const/4 v3, 0x0

    const/4 v5, 0x0

    move-object/from16 v0, p0

    move/from16 v2, p1

    move/from16 v4, p2

    invoke-virtual/range {v0 .. v5}, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->measureChildWithMargins(Landroid/view/View;IIII)V

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mPrivacyContainer:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->getMeasuredWidth()I

    move-result v0

    invoke-direct/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->getPrivacyContainerMarginStart()I

    move-result v1

    add-int v11, v0, v1

    const/4 v0, 0x0

    iget-object v1, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mPrivacyContainer:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    invoke-static {v0, v1}, Ljava/lang/Math;->max(II)I

    move-result v12

    :cond_64
    move v14, v12

    move v15, v11

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mStatusIcons:Landroid/view/View;

    if-eqz v0, :cond_a1

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mStatusIcons:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->getVisibility()I

    move-result v0

    if-eq v0, v13, :cond_a1

    iget-object v1, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mStatusIcons:Landroid/view/View;

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mNotificationIcons:Landroid/view/ViewGroup;

    if-eqz v0, :cond_85

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mNotificationIcons:Landroid/view/ViewGroup;

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v0

    if-lez v0, :cond_85

    div-int/lit8 v0, v9, 0x2

    sub-int/2addr v0, v15

    move v3, v0

    goto :goto_86

    :cond_85
    move v3, v15

    :goto_86
    const/4 v5, 0x0

    move-object/from16 v0, p0

    move/from16 v2, p1

    move/from16 v4, p2

    invoke-virtual/range {v0 .. v5}, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->measureChildWithMargins(Landroid/view/View;IIII)V

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mStatusIcons:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->getMeasuredWidth()I

    move-result v0

    add-int/2addr v15, v0

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mStatusIcons:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->getMeasuredHeight()I

    move-result v0

    invoke-static {v14, v0}, Ljava/lang/Math;->max(II)I

    move-result v14

    :cond_a1
    move/from16 v16, v15

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mNotificationIcons:Landroid/view/ViewGroup;

    if-eqz v0, :cond_d2

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mNotificationIcons:Landroid/view/ViewGroup;

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getVisibility()I

    move-result v0

    if-ne v0, v13, :cond_b0

    goto :goto_d2

    :cond_b0
    iget-object v1, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mNotificationIcons:Landroid/view/ViewGroup;

    const/4 v5, 0x0

    move-object/from16 v0, p0

    move/from16 v2, p1

    move/from16 v3, v16

    move/from16 v4, p2

    invoke-virtual/range {v0 .. v5}, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->measureChildWithMargins(Landroid/view/View;IIII)V

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mNotificationIcons:Landroid/view/ViewGroup;

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getMeasuredWidth()I

    move-result v0

    add-int v0, v16, v0

    iget-object v1, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->mNotificationIcons:Landroid/view/ViewGroup;

    invoke-virtual {v1}, Landroid/view/ViewGroup;->getMeasuredHeight()I

    move-result v1

    invoke-static {v14, v1}, Ljava/lang/Math;->max(II)I

    move-result v14

    move v1, v0

    goto :goto_d4

    :cond_d2
    :goto_d2
    move/from16 v1, v16

    :goto_d4
    const/high16 v0, -0x80000000

    const/high16 v2, 0x40000000  # 2.0f

    if-eq v7, v2, :cond_e3

    if-ne v7, v0, :cond_e1

    invoke-static {v1, v9}, Ljava/lang/Math;->min(II)I

    move-result v3

    goto :goto_e2

    :cond_e1
    move v3, v1

    :goto_e2
    move v9, v3

    :cond_e3
    if-eq v8, v2, :cond_ee

    if-ne v8, v0, :cond_ec

    invoke-static {v14, v10}, Ljava/lang/Math;->min(II)I

    move-result v0

    goto :goto_ed

    :cond_ec
    move v0, v14

    :goto_ed
    move v10, v0

    :cond_ee
    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->getPaddingEnd()I

    move-result v0

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->getPaddingStart()I

    move-result v2

    add-int/2addr v0, v2

    add-int/2addr v0, v9

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->getPaddingEnd()I

    move-result v2

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->getPaddingTop()I

    move-result v3

    add-int/2addr v2, v3

    add-int/2addr v2, v10

    invoke-virtual {v6, v0, v2}, Lcom/android/systemui/newstatusbar/layouts/MiuiNotificationStatusContainer;->setMeasuredDimension(II)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_MiuiNotificationStatusContainer',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
