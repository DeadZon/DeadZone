"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/ext/ExtIconAlpha.smali'
CLASS_FALLBACK_NAMES = ['ExtIconAlpha.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public abstract Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;
.super Lcom/android/systemui/statusbar/AlphaOptimizedImageView;


# instance fields
.field protected curHeight:I

.field protected curWidth:I

.field protected final isCustColor:Z

.field protected isIconAdded:Z

.field protected mIconSize:I

.field protected sizeRatio:F

.field private tint:Landroid/content/res/ColorStateList;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    const/4 v0, 0x0

    invoke-direct {p0, p1, v0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    const/4 v0, 0x0

    invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    const/4 v0, 0x0

    invoke-direct {p0, p1, p2, p3, v0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V
    .registers 8

    invoke-direct {p0, p1, p2, p3, p4}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    const/4 v0, 0x0

    iput v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->curWidth:I

    iput v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->curHeight:I

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->isIconAdded:Z

    const/high16 v1, 0x3f800000  # 1.0f

    iput v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->sizeRatio:F

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    const-string v2, "status_bar_icon_height"

    invoke-static {p1, v2}, Landroid/Utils/Utils;->DimenToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v2

    invoke-virtual {v1, v2}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v1

    iput v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->mIconSize:I

    const-string v1, "use_config_color_size_element"

    invoke-static {p1, v1}, Landroid/Utils/Utils;->BoolToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    if-eqz v1, :cond_30

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    invoke-virtual {v2, v1}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v2

    if-eqz v2, :cond_31

    :cond_30
    const/4 v0, 0x1

    :cond_31
    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->isCustColor:Z

    return-void
.end method

.method private drawInternal(Landroid/graphics/Canvas;Lcom/android/systemui/newstatusbar/data/IconData;)V
    .registers 7

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    iget v1, p2, Lcom/android/systemui/newstatusbar/data/IconData;->color:I

    const/4 v2, 0x0

    if-nez v1, :cond_12

    invoke-virtual {v0, v2}, Landroid/graphics/drawable/Drawable;->setColorFilter(Landroid/graphics/ColorFilter;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->tint:Landroid/content/res/ColorStateList;

    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->setTintList(Landroid/content/res/ColorStateList;)V

    goto :goto_21

    :cond_12
    invoke-virtual {v0, v2}, Landroid/graphics/drawable/Drawable;->setTintList(Landroid/content/res/ColorStateList;)V

    new-instance v1, Landroid/graphics/PorterDuffColorFilter;

    iget v2, p2, Lcom/android/systemui/newstatusbar/data/IconData;->color:I

    sget-object v3, Landroid/graphics/PorterDuff$Mode;->SRC_IN:Landroid/graphics/PorterDuff$Mode;

    invoke-direct {v1, v2, v3}, Landroid/graphics/PorterDuffColorFilter;-><init>(ILandroid/graphics/PorterDuff$Mode;)V

    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->setColorFilter(Landroid/graphics/ColorFilter;)V

    :goto_21
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->getWidth()I

    move-result v1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->getHeight()I

    move-result v2

    const/4 v3, 0x0

    invoke-virtual {v0, v3, v3, v1, v2}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    invoke-virtual {v0, p1}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    return-void
.end method

.method private updateScale(Landroid/graphics/Canvas;Lcom/android/systemui/newstatusbar/data/IconData;)V
    .registers 9

    iget v0, p2, Lcom/android/systemui/newstatusbar/data/IconData;->zoom:I

    int-to-float v0, v0

    const/high16 v1, 0x42c80000  # 100.0f

    div-float v0, v1, v0

    const/high16 v2, 0x3f800000  # 1.0f

    sub-float/2addr v0, v2

    const/high16 v2, 0x40800000  # 4.0f

    mul-float/2addr v0, v2

    iget v2, p2, Lcom/android/systemui/newstatusbar/data/IconData;->division:I

    int-to-float v2, v2

    add-float/2addr v2, v0

    const/4 v3, 0x0

    invoke-virtual {p1, v3, v2}, Landroid/graphics/Canvas;->translate(FF)V

    iget v2, p2, Lcom/android/systemui/newstatusbar/data/IconData;->scale:I

    int-to-float v2, v2

    div-float/2addr v2, v1

    iget v3, p2, Lcom/android/systemui/newstatusbar/data/IconData;->scale:I

    int-to-float v3, v3

    div-float/2addr v3, v1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->getWidth()I

    move-result v1

    int-to-float v1, v1

    const/high16 v4, 0x40000000  # 2.0f

    div-float/2addr v1, v4

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->getHeight()I

    move-result v5

    int-to-float v5, v5

    div-float/2addr v5, v4

    invoke-virtual {p1, v2, v3, v1, v5}, Landroid/graphics/Canvas;->scale(FFFF)V

    return-void
.end method

.method private updateSizeRatio(Landroid/graphics/drawable/Drawable;)V
    .registers 4

    invoke-virtual {p1}, Landroid/graphics/drawable/Drawable;->getIntrinsicWidth()I

    move-result v0

    int-to-float v0, v0

    invoke-virtual {p1}, Landroid/graphics/drawable/Drawable;->getIntrinsicHeight()I

    move-result v1

    int-to-float v1, v1

    div-float/2addr v0, v1

    iput v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->sizeRatio:F

    return-void
.end method

.method private updateZoom()V
    .registers 2

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    if-eqz v0, :cond_9

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    :cond_9
    return-void
.end method


# virtual methods
.method public abstract getData()Lcom/android/systemui/newstatusbar/data/IconData;
.end method

.method protected abstract onAttached()V
.end method

.method protected onAttachedToWindow()V
    .registers 1

    goto/32 :goto_c

    nop

    :goto_4
    return-void

    :goto_5
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->onAttached()V

    goto/32 :goto_4

    nop

    :goto_c
    invoke-super {p0}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;->onAttachedToWindow()V

    goto/32 :goto_5

    nop
.end method

.method protected abstract onDetached()V
.end method

.method protected onDetachedFromWindow()V
    .registers 1

    goto/32 :goto_c

    nop

    :goto_4
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->onDetached()V

    goto/32 :goto_b

    nop

    :goto_b
    return-void

    :goto_c
    invoke-super {p0}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;->onDetachedFromWindow()V

    goto/32 :goto_4

    nop
.end method

.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 4

    goto/32 :goto_19

    nop

    :goto_4
    if-nez v0, :cond_9

    goto/32 :goto_e

    :cond_9
    goto/32 :goto_41

    nop

    :goto_d
    return-void

    :goto_e
    goto/32 :goto_12

    nop

    :goto_12
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;->onDraw(Landroid/graphics/Canvas;)V

    goto/32 :goto_4f

    nop

    :goto_19
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->isCustColor:Z

    goto/32 :goto_38

    nop

    :goto_1f
    if-nez v1, :cond_24

    goto/32 :goto_e

    :cond_24
    goto/32 :goto_4

    nop

    :goto_28
    if-nez v1, :cond_2d

    goto/32 :goto_e

    :cond_2d
    goto/32 :goto_31

    nop

    :goto_31
    invoke-direct {p0, p1, v0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->updateScale(Landroid/graphics/Canvas;Lcom/android/systemui/newstatusbar/data/IconData;)V

    goto/32 :goto_50

    nop

    :goto_38
    if-nez v0, :cond_3d

    goto/32 :goto_e

    :cond_3d
    goto/32 :goto_57

    nop

    :goto_41
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v1

    goto/32 :goto_28

    nop

    :goto_49
    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->isIconAdded:Z

    goto/32 :goto_1f

    nop

    :goto_4f
    return-void

    :goto_50
    invoke-direct {p0, p1, v0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->drawInternal(Landroid/graphics/Canvas;Lcom/android/systemui/newstatusbar/data/IconData;)V

    goto/32 :goto_d

    nop

    :goto_57
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->getData()Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    goto/32 :goto_49

    nop
.end method

.method public setImageDrawable(Landroid/graphics/drawable/Drawable;)V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->isCustColor:Z

    if-eqz v0, :cond_13

    if-eqz p1, :cond_13

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->isIconAdded:Z

    if-nez v0, :cond_13

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->updateSizeRatio(Landroid/graphics/drawable/Drawable;)V

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->isIconAdded:Z

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->update()V

    :cond_13
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    return-void
.end method

.method public setImageResource(I)V
    .registers 4

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->isCustColor:Z

    if-eqz v0, :cond_25

    if-eqz p1, :cond_25

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->isIconAdded:Z

    if-nez v0, :cond_25

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-virtual {v1}, Landroid/content/Context;->getTheme()Landroid/content/res/Resources$Theme;

    move-result-object v1

    invoke-virtual {v0, p1, v1}, Landroid/content/res/Resources;->getDrawable(ILandroid/content/res/Resources$Theme;)Landroid/graphics/drawable/Drawable;

    move-result-object v0

    if-eqz v0, :cond_25

    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->updateSizeRatio(Landroid/graphics/drawable/Drawable;)V

    const/4 v1, 0x1

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->isIconAdded:Z

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->update()V

    :cond_25
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;->setImageResource(I)V

    return-void
.end method

.method public setImageTintList(Landroid/content/res/ColorStateList;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->tint:Landroid/content/res/ColorStateList;

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;->setImageTintList(Landroid/content/res/ColorStateList;)V

    return-void
.end method

.method public setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V
    .registers 6

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->isCustColor:Z

    if-eqz v0, :cond_2a

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->getData()Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->isIconAdded:Z

    if-eqz v1, :cond_2a

    if-eqz v0, :cond_2a

    if-eqz p1, :cond_2a

    iget v1, v0, Lcom/android/systemui/newstatusbar/data/IconData;->zoom:I

    int-to-float v2, v1

    iget v3, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->mIconSize:I

    int-to-float v3, v3

    mul-float/2addr v2, v3

    const/high16 v3, 0x42c80000  # 100.0f

    div-float/2addr v2, v3

    float-to-int v2, v2

    iput v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->curHeight:I

    int-to-float v2, v2

    iget v3, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->sizeRatio:F

    mul-float/2addr v2, v3

    float-to-int v2, v2

    iput v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->curWidth:I

    iput v2, p1, Landroid/view/ViewGroup$LayoutParams;->width:I

    iget v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->curHeight:I

    iput v2, p1, Landroid/view/ViewGroup$LayoutParams;->height:I

    :cond_2a
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    return-void
.end method

.method public setScaleType(Landroid/widget/ImageView$ScaleType;)V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->isCustColor:Z

    if-nez v0, :cond_7

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;->setScaleType(Landroid/widget/ImageView$ScaleType;)V

    :cond_7
    return-void
.end method

.method public update()V
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->isIconAdded:Z

    if-eqz v0, :cond_e

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->isCustColor:Z

    if-eqz v0, :cond_e

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->updateZoom()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;->invalidate()V

    :cond_e
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_ext_ExtIconAlpha',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
