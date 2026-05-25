"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/sim/MobileTypeDrawable.smali'
CLASS_FALLBACK_NAMES = ['MobileTypeDrawable.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;
.super Lcom/android/systemui/statusbar/views/MobileTypeDrawable;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;


# instance fields
.field protected controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

.field private parent:Lcom/android/systemui/newstatusbar/sim/MobileTypeImageView;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/views/MobileTypeDrawable;-><init>(Landroid/content/Context;)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    return-void
.end method

.method public static updateMobileTypeLayoutParams(Lcom/android/systemui/statusbar/views/MobileTypeDrawable;Ljava/lang/String;ZZLandroid/widget/ImageView;Landroid/widget/ImageView;Landroid/view/ViewGroup;)V
    .registers 16

    if-nez p1, :cond_4

    if-eqz p2, :cond_68

    :cond_4
    move-object v0, p0

    check-cast v0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->measure()V

    iget v1, v0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mHeight:I

    iget v2, v0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mExtraWidth:I

    iget v3, v0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mWidth:I

    add-int/2addr v2, v3

    invoke-virtual {p4}, Landroid/widget/ImageView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v3

    check-cast v3, Landroid/widget/FrameLayout$LayoutParams;

    iget v4, v3, Landroid/widget/FrameLayout$LayoutParams;->width:I

    if-ne v4, v2, :cond_1f

    iget v4, v3, Landroid/widget/FrameLayout$LayoutParams;->height:I

    if-eq v4, v1, :cond_26

    :cond_1f
    iput v2, v3, Landroid/widget/FrameLayout$LayoutParams;->width:I

    iput v1, v3, Landroid/widget/FrameLayout$LayoutParams;->height:I

    invoke-virtual {p4, v3}, Landroid/widget/ImageView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    :cond_26
    instance-of v4, p6, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;

    if-eqz v4, :cond_68

    move-object v4, p6

    check-cast v4, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;

    invoke-virtual {v4}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v5

    check-cast v5, Landroid/widget/LinearLayout$LayoutParams;

    iget-boolean v6, v4, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->isHorizontal:Z

    if-eqz v6, :cond_39

    const/4 v7, 0x1

    goto :goto_3a

    :cond_39
    const/4 v7, 0x2

    :goto_3a
    invoke-virtual {p4}, Landroid/widget/ImageView;->getMeasuredHeight()I

    move-result v8

    mul-int/2addr v7, v8

    invoke-virtual {p5}, Landroid/widget/ImageView;->getMeasuredHeight()I

    move-result v8

    invoke-static {v7, v8}, Ljava/lang/Math;->max(II)I

    move-result v1

    invoke-virtual {p4}, Landroid/widget/ImageView;->getMeasuredWidth()I

    move-result v2

    if-nez v6, :cond_56

    iget-object v7, p0, Lcom/android/systemui/statusbar/views/MobileTypeDrawable;->mMobileTypeTextPaint:Landroid/graphics/Paint;

    const-string v8, "4G+"

    invoke-virtual {v7, v8}, Landroid/graphics/Paint;->measureText(Ljava/lang/String;)F

    move-result v7

    float-to-int v2, v7

    :cond_56
    if-eqz v6, :cond_5d

    invoke-virtual {p5}, Landroid/widget/ImageView;->getMeasuredWidth()I

    move-result v7

    add-int/2addr v2, v7

    :cond_5d
    if-nez v6, :cond_61

    mul-int/lit8 v1, v1, 0x2

    :cond_61
    iput v1, v5, Landroid/widget/LinearLayout$LayoutParams;->height:I

    iput v2, v5, Landroid/widget/LinearLayout$LayoutParams;->width:I

    invoke-virtual {p6, v5}, Landroid/view/ViewGroup;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    :cond_68
    return-void
.end method


# virtual methods
.method public draw(Landroid/graphics/Canvas;)V
    .registers 10

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mMobileType:Ljava/lang/String;

    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-eqz v0, :cond_9

    return-void

    :cond_9
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->getData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mMobileTypeTextPaint:Landroid/graphics/Paint;

    iget v2, v0, Lcom/android/systemui/newstatusbar/data/TextData;->color:I

    if-nez v2, :cond_16

    iget v2, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mMobileTypeColor:I

    goto :goto_1a

    :cond_16
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/TextData;->getColor()I

    move-result v2

    :goto_1a
    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setColor(I)V

    iget v2, v0, Lcom/android/systemui/newstatusbar/data/TextData;->division:I

    int-to-float v2, v2

    const/high16 v3, 0x41200000  # 10.0f

    div-float/2addr v2, v3

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->getIntrinsicHeight()I

    move-result v3

    int-to-float v3, v3

    const/high16 v4, 0x40000000  # 2.0f

    div-float/2addr v3, v4

    invoke-virtual {v1}, Landroid/graphics/Paint;->descent()F

    move-result v4

    invoke-virtual {v1}, Landroid/graphics/Paint;->ascent()F

    move-result v5

    add-float/2addr v4, v5

    div-float/2addr v4, v2

    sub-float/2addr v3, v4

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mMobileType:Ljava/lang/String;

    const/4 v5, 0x0

    invoke-virtual {p1, v4, v5, v3, v1}, Landroid/graphics/Canvas;->drawText(Ljava/lang/String;FFLandroid/graphics/Paint;)V

    iget-boolean v4, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mShowMobileTypeDoublePlus:Z

    if-eqz v4, :cond_5e

    iget v4, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mWidth:I

    int-to-float v4, v4

    iget v5, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mHeight:I

    int-to-float v5, v5

    const/high16 v6, 0x40800000  # 4.0f

    add-float/2addr v5, v6

    iget-object v6, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mMobileTypePlusPaint:Landroid/graphics/Paint;

    const-string v7, "+"

    invoke-virtual {p1, v7, v4, v5, v6}, Landroid/graphics/Canvas;->drawText(Ljava/lang/String;FFLandroid/graphics/Paint;)V

    iget v4, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mWidth:I

    int-to-float v4, v4

    iget v5, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mHeight:I

    int-to-float v5, v5

    const/high16 v6, 0x40e00000  # 7.0f

    sub-float/2addr v5, v6

    iget-object v6, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mMobileTypePlusPaint:Landroid/graphics/Paint;

    invoke-virtual {p1, v7, v4, v5, v6}, Landroid/graphics/Canvas;->drawText(Ljava/lang/String;FFLandroid/graphics/Paint;)V

    :cond_5e
    return-void
.end method

.method protected getData()Lcom/android/systemui/newstatusbar/data/TextData;
    .registers 2

    goto/32 :goto_22

    nop

    :goto_4
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->getSimTypeData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    goto/32 :goto_15

    nop

    :goto_c
    if-eqz v0, :cond_11

    goto/32 :goto_1e

    :cond_11
    goto/32 :goto_30

    nop

    :goto_15
    return-object v0

    :goto_16
    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    goto/32 :goto_1c

    nop

    :goto_1c
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    :goto_1e
    goto/32 :goto_36

    nop

    :goto_22
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    goto/32 :goto_c

    nop

    :goto_28
    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    goto/32 :goto_16

    nop

    :goto_30
    const-class v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    goto/32 :goto_28

    nop

    :goto_36
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    goto/32 :goto_4

    nop
.end method

.method public measure()V
    .registers 5

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->getData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->updateTypefase(Lcom/android/systemui/newstatusbar/data/TextData;)V

    iget v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->zoom:I

    if-nez v1, :cond_e

    iget v1, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mMobileTypeSize:I

    goto :goto_10

    :cond_e
    iget v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->zoom:I

    :goto_10
    iput v1, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mMobileTypeSize:I

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mMobileTypeTextPaint:Landroid/graphics/Paint;

    iget v2, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mMobileTypeSize:I

    int-to-float v2, v2

    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setTextSize(F)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mMobileTypePlusPaint:Landroid/graphics/Paint;

    iget v2, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mMobileTypeSize:I

    int-to-float v2, v2

    const v3, 0x3f547ae1  # 0.83f

    mul-float/2addr v2, v3

    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setTextSize(F)V

    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MobileTypeDrawable;->measure()V

    return-void
.end method

.method public onIconChange()V
    .registers 2

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->measure()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->parent:Lcom/android/systemui/newstatusbar/sim/MobileTypeImageView;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/sim/MobileTypeImageView;->updateMobileTypeLayout()V

    return-void
.end method

.method public setParent(Lcom/android/systemui/newstatusbar/sim/MobileTypeImageView;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->parent:Lcom/android/systemui/newstatusbar/sim/MobileTypeImageView;

    return-void
.end method

.method public updateTypefase(Lcom/android/systemui/newstatusbar/data/TextData;)V
    .registers 4

    invoke-virtual {p1}, Lcom/android/systemui/newstatusbar/data/TextData;->getTypeFace()Landroid/graphics/Typeface;

    move-result-object v0

    iget v1, p1, Lcom/android/systemui/newstatusbar/data/TextData;->typeFaseStyle:I

    invoke-static {v0, v1}, Landroid/graphics/Typeface;->create(Landroid/graphics/Typeface;I)Landroid/graphics/Typeface;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mMobileTypeTextPaint:Landroid/graphics/Paint;

    invoke-virtual {v1, v0}, Landroid/graphics/Paint;->setTypeface(Landroid/graphics/Typeface;)Landroid/graphics/Typeface;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/sim/MobileTypeDrawable;->mMobileTypePlusPaint:Landroid/graphics/Paint;

    invoke-virtual {v1, v0}, Landroid/graphics/Paint;->setTypeface(Landroid/graphics/Typeface;)Landroid/graphics/Typeface;

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_sim_MobileTypeDrawable',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
