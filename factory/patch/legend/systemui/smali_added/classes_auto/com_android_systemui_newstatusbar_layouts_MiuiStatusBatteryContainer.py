"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer.smali'
CLASS_FALLBACK_NAMES = ['MiuiStatusBatteryContainer.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;
.super Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;


# instance fields
.field TAG:Ljava/lang/String;

.field private layout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

.field private maxWidth:I


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;-><init>(Landroid/content/Context;)V

    const/16 v0, 0xbb8

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->maxWidth:I

    sget-object v0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->TAG:Ljava/lang/String;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->TAG:Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const/16 v0, 0xbb8

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->maxWidth:I

    sget-object v0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->TAG:Ljava/lang/String;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->TAG:Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const/16 v0, 0xbb8

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->maxWidth:I

    sget-object v0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->TAG:Ljava/lang/String;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->TAG:Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V
    .registers 6

    invoke-direct {p0, p1, p2, p3, p4}, Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    const/16 v0, 0xbb8

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->maxWidth:I

    sget-object v0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->TAG:Ljava/lang/String;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->TAG:Ljava/lang/String;

    return-void
.end method


# virtual methods
.method public onLayout(ZIIII)V
    .registers 23

    move-object/from16 v0, p0

    iget-object v1, v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mBattery:Landroid/view/View;

    if-eqz v1, :cond_a

    invoke-super/range {p0 .. p5}, Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;->onLayout(ZIIII)V

    return-void

    :cond_a
    const/4 v1, 0x0

    sub-int v2, p5, p3

    sub-int v3, p4, p2

    iget-object v4, v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mHomePrivacyContainer:Landroid/view/View;

    const/16 v5, 0x8

    if-eqz v4, :cond_55

    invoke-virtual {v4}, Landroid/view/View;->getVisibility()I

    move-result v7

    if-ne v7, v5, :cond_1c

    goto :goto_55

    :cond_1c
    iget-object v7, v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mHomePrivacyContainer:Landroid/view/View;

    invoke-virtual {v7}, Landroid/view/View;->getMeasuredWidth()I

    move-result v7

    iget-object v8, v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mHomePrivacyContainer:Landroid/view/View;

    invoke-virtual {v8}, Landroid/view/View;->getMeasuredHeight()I

    move-result v8

    iget-object v9, v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mHomePrivacyContainer:Landroid/view/View;

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->getPaddingEnd()I

    move-result v10

    sub-int v11, v3, v10

    sub-int/2addr v11, v7

    if-le v8, v2, :cond_35

    const/4 v10, 0x0

    goto :goto_39

    :cond_35
    sub-int v10, v2, v8

    div-int/lit8 v10, v10, 0x2

    :goto_39
    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->getPaddingTop()I

    move-result v12

    add-int/2addr v10, v12

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->getPaddingEnd()I

    move-result v12

    sub-int v13, v3, v12

    if-le v8, v2, :cond_48

    move v14, v2

    goto :goto_4c

    :cond_48
    add-int v14, v2, v8

    div-int/lit8 v14, v14, 0x2

    :goto_4c
    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->getPaddingBottom()I

    move-result v15

    add-int/2addr v14, v15

    invoke-virtual {v9, v11, v10, v13, v14}, Landroid/view/View;->layout(IIII)V

    goto :goto_57

    :cond_55
    :goto_55
    const/4 v7, 0x0

    const/4 v8, 0x0

    :goto_57
    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->getPaddingStart()I

    move-result v9

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->getPaddingEnd()I

    move-result v10

    sub-int v11, v3, v10

    iget-object v12, v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mPrivacyState:Lcom/android/systemui/statusbar/phone/MiuiHomePrivacyController$PrivacyState;

    sget-object v13, Lcom/android/systemui/statusbar/phone/MiuiHomePrivacyController$PrivacyState;->START_SHOW_PRIVACY:Lcom/android/systemui/statusbar/phone/MiuiHomePrivacyController$PrivacyState;

    if-eq v12, v13, :cond_6b

    sget-object v13, Lcom/android/systemui/statusbar/phone/MiuiHomePrivacyController$PrivacyState;->COMPLETE_SHOW_PRIVACY:Lcom/android/systemui/statusbar/phone/MiuiHomePrivacyController$PrivacyState;

    if-ne v12, v13, :cond_6d

    :cond_6b
    sub-int/2addr v11, v7

    move v1, v8

    :cond_6d
    iget-object v13, v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mStatusIcon:Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;

    if-eqz v13, :cond_a6

    invoke-virtual {v13}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;->getVisibility()I

    move-result v14

    if-eq v14, v5, :cond_a6

    if-nez v1, :cond_7f

    iget-object v5, v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mStatusIcon:Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;

    invoke-virtual {v5}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;->getMeasuredHeight()I

    move-result v1

    :cond_7f
    iget-object v5, v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mStatusIcon:Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;

    iget-boolean v14, v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mBatteryChanged:Z

    invoke-virtual {v5, v14}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;->setBatteryChanged(Z)V

    iget-object v5, v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mStatusIcon:Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;

    if-le v1, v2, :cond_8c

    const/4 v14, 0x0

    goto :goto_90

    :cond_8c
    sub-int v14, v2, v1

    div-int/lit8 v14, v14, 0x2

    :goto_90
    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->getPaddingTop()I

    move-result v15

    add-int/2addr v14, v15

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->getPaddingBottom()I

    move-result v15

    if-gt v1, v2, :cond_a1

    add-int v16, v2, v1

    div-int/lit8 v16, v16, 0x2

    move/from16 v2, v16

    :cond_a1
    add-int v6, v2, v15

    invoke-virtual {v5, v9, v14, v11, v6}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;->layout(IIII)V

    :cond_a6
    const/4 v5, 0x0

    iput-boolean v5, v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mBatteryChanged:Z

    return-void
.end method

.method public onMeasure(II)V
    .registers 23

    move-object/from16 v6, p0

    invoke-static/range {p1 .. p1}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result v7

    invoke-static/range {p2 .. p2}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result v8

    invoke-static/range {p1 .. p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v9

    invoke-static/range {p2 .. p2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v10

    iget-object v11, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mHomePrivacyContainer:Landroid/view/View;

    sget-object v12, Lcom/android/systemui/statusbar/phone/MiuiHomePrivacyController$PrivacyState;->COMPLETE_SHOW_PRIVACY:Lcom/android/systemui/statusbar/phone/MiuiHomePrivacyController$PrivacyState;

    sget-object v13, Lcom/android/systemui/statusbar/phone/MiuiHomePrivacyController$PrivacyState;->START_SHOW_PRIVACY:Lcom/android/systemui/statusbar/phone/MiuiHomePrivacyController$PrivacyState;

    const/4 v14, 0x0

    const/4 v15, 0x0

    if-eqz v11, :cond_52

    invoke-virtual {v11}, Landroid/view/View;->getVisibility()I

    move-result v0

    const/16 v1, 0x8

    if-ne v0, v1, :cond_25

    goto :goto_52

    :cond_25
    const/16 v16, 0x8

    iget-object v1, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mHomePrivacyContainer:Landroid/view/View;

    const/4 v3, 0x0

    const/4 v5, 0x0

    move-object/from16 v0, p0

    move/from16 v2, p1

    move/from16 v4, p2

    invoke-virtual/range {v0 .. v5}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->measureChildWithMargins(Landroid/view/View;IIII)V

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mPrivacyState:Lcom/android/systemui/statusbar/phone/MiuiHomePrivacyController$PrivacyState;

    if-eq v0, v13, :cond_3e

    if-ne v0, v12, :cond_3b

    goto :goto_3e

    :cond_3b
    move/from16 v5, v16

    goto :goto_56

    :cond_3e
    :goto_3e
    iget-object v1, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mHomePrivacyContainer:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v14

    const/4 v1, 0x0

    iget-object v2, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mHomePrivacyContainer:Landroid/view/View;

    invoke-virtual {v2}, Landroid/view/View;->getMeasuredHeight()I

    move-result v2

    invoke-static {v1, v2}, Ljava/lang/Math;->max(II)I

    move-result v15

    move/from16 v5, v16

    goto :goto_56

    :cond_52
    :goto_52
    const/16 v16, 0x8

    move/from16 v5, v16

    :goto_56
    iget-object v4, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mBattery:Landroid/view/View;

    if-eqz v4, :cond_92

    invoke-virtual {v4}, Landroid/view/View;->getVisibility()I

    move-result v0

    if-eq v0, v5, :cond_92

    iget-object v1, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mBattery:Landroid/view/View;

    const/16 v16, 0x0

    move-object/from16 v0, p0

    move/from16 v2, p1

    move v3, v14

    move-object/from16 v17, v4

    move/from16 v4, p2

    move-object/from16 v18, v11

    move v11, v5

    move/from16 v5, v16

    invoke-virtual/range {v0 .. v5}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->measureChildWithMargins(Landroid/view/View;IIII)V

    iget-boolean v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mIsHideBattery:Z

    if-eqz v0, :cond_80

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mPrivacyState:Lcom/android/systemui/statusbar/phone/MiuiHomePrivacyController$PrivacyState;

    move-object v1, v0

    if-eq v0, v13, :cond_97

    if-eq v1, v12, :cond_97

    :cond_80
    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mBattery:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->getMeasuredWidth()I

    move-result v0

    add-int/2addr v14, v0

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mBattery:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->getMeasuredHeight()I

    move-result v0

    invoke-static {v15, v0}, Ljava/lang/Math;->max(II)I

    move-result v15

    goto :goto_97

    :cond_92
    move-object/from16 v17, v4

    move-object/from16 v18, v11

    move v11, v5

    :cond_97
    :goto_97
    iget-object v5, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mStatusIcon:Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;

    if-eqz v5, :cond_c5

    invoke-virtual {v5}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;->getVisibility()I

    move-result v0

    if-eq v0, v11, :cond_c5

    iget-object v1, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mStatusIcon:Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;

    const/16 v16, 0x0

    move-object/from16 v0, p0

    move/from16 v2, p1

    move v3, v14

    move/from16 v4, p2

    move-object/from16 v19, v5

    move/from16 v5, v16

    invoke-virtual/range {v0 .. v5}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->measureChildWithMargins(Landroid/view/View;IIII)V

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mStatusIcon:Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;

    invoke-virtual {v0}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;->getMeasuredWidth()I

    move-result v0

    add-int/2addr v14, v0

    iget-object v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mStatusIcon:Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;

    invoke-virtual {v0}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;->getMeasuredHeight()I

    move-result v0

    invoke-static {v15, v0}, Ljava/lang/Math;->max(II)I

    move-result v15

    goto :goto_c7

    :cond_c5
    move-object/from16 v19, v5

    :goto_c7
    const/high16 v0, -0x80000000

    const/high16 v1, 0x40000000  # 2.0f

    if-eq v7, v1, :cond_d6

    if-ne v7, v0, :cond_d4

    invoke-static {v14, v9}, Ljava/lang/Math;->min(II)I

    move-result v2

    goto :goto_d5

    :cond_d4
    move v2, v14

    :goto_d5
    move v9, v2

    :cond_d6
    if-eq v8, v1, :cond_e1

    if-ne v8, v0, :cond_df

    invoke-static {v15, v10}, Ljava/lang/Math;->min(II)I

    move-result v0

    goto :goto_e0

    :cond_df
    move v0, v15

    :goto_e0
    move v10, v0

    :cond_e1
    iget v0, v6, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->maxWidth:I

    invoke-static {v9, v0}, Ljava/lang/Math;->min(II)I

    move-result v0

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->getPaddingTop()I

    move-result v1

    add-int/2addr v1, v10

    invoke-virtual {v6, v0, v1}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->setMeasuredDimension(II)V

    return-void
.end method

.method public setMaxWidth(I)V
    .registers 3

    iput p1, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->maxWidth:I

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mStatusIcon:Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;

    instance-of v0, v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;

    if-eqz v0, :cond_f

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->mStatusIcon:Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;

    check-cast v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->setIsKeyguard()V

    :cond_f
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_MiuiStatusBatteryContainer',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
