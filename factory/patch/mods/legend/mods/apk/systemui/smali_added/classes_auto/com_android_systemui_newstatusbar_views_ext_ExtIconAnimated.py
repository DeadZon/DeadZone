"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/ext/ExtIconAnimated.smali'
CLASS_FALLBACK_NAMES = ['ExtIconAnimated.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public abstract Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;
.super Lcom/android/systemui/statusbar/AnimatedImageView;


# instance fields
.field TAG:Ljava/lang/String;

.field private colorFilter:Landroid/graphics/ColorFilter;

.field protected curHeight:I

.field protected curWidth:I

.field protected final isCustColor:Z

.field private isIconAdded:Z

.field protected isNeedZoom:Z

.field protected mIconSize:I

.field protected sizeRatio:F

.field private tint:Landroid/content/res/ColorStateList;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 7

    const/4 v2, 0x1

    const/4 v1, 0x0

    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/AnimatedImageView;-><init>(Landroid/content/Context;)V

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isIconAdded:Z

    const/high16 v3, 0x3f800000  # 1.0f

    iput v3, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->sizeRatio:F

    iput-boolean v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isNeedZoom:Z

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->getContext()Landroid/content/Context;

    move-result-object p1

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v3

    const-string v4, "status_bar_icon_height"

    invoke-static {p1, v4}, Landroid/Utils/Utils;->DimenToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v4

    invoke-virtual {v3, v4}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v3

    iput v3, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->mIconSize:I

    const-string v3, "use_config_color_size_element"

    invoke-static {p1, v3}, Landroid/Utils/Utils;->BoolToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    if-eqz v0, :cond_33

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v3

    invoke-virtual {v3, v0}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v3

    if-eqz v3, :cond_34

    :cond_33
    move v1, v2

    :cond_34
    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isCustColor:Z

    const v1, -0xff0100

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->setBackgroundColor(I)V

    const-string v1, "Nastya23"

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->TAG:Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 8

    const/4 v2, 0x1

    const/4 v1, 0x0

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/AnimatedImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isIconAdded:Z

    const/high16 v3, 0x3f800000  # 1.0f

    iput v3, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->sizeRatio:F

    iput-boolean v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isNeedZoom:Z

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->getContext()Landroid/content/Context;

    move-result-object p1

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v3

    const-string v4, "status_bar_icon_height"

    invoke-static {p1, v4}, Landroid/Utils/Utils;->DimenToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v4

    invoke-virtual {v3, v4}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v3

    iput v3, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->mIconSize:I

    const-string v3, "use_config_color_size_element"

    invoke-static {p1, v3}, Landroid/Utils/Utils;->BoolToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    if-eqz v0, :cond_33

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v3

    invoke-virtual {v3, v0}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v3

    if-eqz v3, :cond_34

    :cond_33
    move v1, v2

    :cond_34
    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isCustColor:Z

    const v1, -0xff0100

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->setBackgroundColor(I)V

    const-string v1, "Nastya23"

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->TAG:Ljava/lang/String;

    return-void
.end method

.method private drawInternal(Landroid/graphics/Canvas;Lcom/android/systemui/newstatusbar/data/IconData;)V
    .registers 8

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v1

    iget v2, p2, Lcom/android/systemui/newstatusbar/data/IconData;->color:I

    if-nez v2, :cond_2a

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->colorFilter:Landroid/graphics/ColorFilter;

    invoke-virtual {v1, v2}, Landroid/graphics/drawable/Drawable;->setColorFilter(Landroid/graphics/ColorFilter;)V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->tint:Landroid/content/res/ColorStateList;

    invoke-virtual {v1, v2}, Landroid/graphics/drawable/Drawable;->setTintList(Landroid/content/res/ColorStateList;)V

    :goto_12
    const/4 v0, 0x0

    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isNeedZoom:Z

    if-nez v2, :cond_19

    const/16 v0, 0xa

    :cond_19
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->getMeasuredWidth()I

    move-result v2

    sub-int/2addr v2, v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->getMeasuredHeight()I

    move-result v3

    sub-int/2addr v3, v0

    invoke-virtual {v1, v0, v0, v2, v3}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    invoke-virtual {v1, p1}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    return-void

    :cond_2a
    const/4 v2, 0x0

    invoke-virtual {v1, v2}, Landroid/graphics/drawable/Drawable;->setTintList(Landroid/content/res/ColorStateList;)V

    new-instance v2, Landroid/graphics/PorterDuffColorFilter;

    iget v3, p2, Lcom/android/systemui/newstatusbar/data/IconData;->color:I

    sget-object v4, Landroid/graphics/PorterDuff$Mode;->SRC_IN:Landroid/graphics/PorterDuff$Mode;

    invoke-direct {v2, v3, v4}, Landroid/graphics/PorterDuffColorFilter;-><init>(ILandroid/graphics/PorterDuff$Mode;)V

    invoke-virtual {v1, v2}, Landroid/graphics/drawable/Drawable;->setColorFilter(Landroid/graphics/ColorFilter;)V

    goto :goto_12
.end method

.method private updateScale(Landroid/graphics/Canvas;Lcom/android/systemui/newstatusbar/data/IconData;)V
    .registers 9

    const/high16 v5, 0x40000000  # 2.0f

    const/high16 v3, 0x42c80000  # 100.0f

    iget v1, p2, Lcom/android/systemui/newstatusbar/data/IconData;->zoom:I

    int-to-float v1, v1

    div-float v1, v3, v1

    const/high16 v2, 0x3f800000  # 1.0f

    sub-float/2addr v1, v2

    const/high16 v2, 0x40800000  # 4.0f

    mul-float v0, v1, v2

    const/4 v1, 0x0

    iget v2, p2, Lcom/android/systemui/newstatusbar/data/IconData;->division:I

    int-to-float v2, v2

    add-float/2addr v2, v0

    invoke-virtual {p1, v1, v2}, Landroid/graphics/Canvas;->translate(FF)V

    iget v1, p2, Lcom/android/systemui/newstatusbar/data/IconData;->scale:I

    int-to-float v1, v1

    div-float/2addr v1, v3

    iget v2, p2, Lcom/android/systemui/newstatusbar/data/IconData;->scale:I

    int-to-float v2, v2

    div-float/2addr v2, v3

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->getMeasuredWidth()I

    move-result v3

    int-to-float v3, v3

    div-float/2addr v3, v5

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->getMeasuredHeight()I

    move-result v4

    int-to-float v4, v4

    div-float/2addr v4, v5

    invoke-virtual {p1, v1, v2, v3, v4}, Landroid/graphics/Canvas;->scale(FFFF)V

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

    iput v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->sizeRatio:F

    return-void
.end method

.method private updateZoom()V
    .registers 3

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isNeedZoom:Z

    if-eqz v1, :cond_d

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    if-eqz v0, :cond_d

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    :cond_d
    return-void
.end method


# virtual methods
.method public draw(Landroid/graphics/Canvas;)V
    .registers 5

    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isCustColor:Z

    if-eqz v2, :cond_22

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->getData()Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v1

    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isIconAdded:Z

    if-eqz v2, :cond_22

    if-eqz v1, :cond_22

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v2

    if-eqz v2, :cond_22

    invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I

    move-result v0

    invoke-direct {p0, p1, v1}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->updateScale(Landroid/graphics/Canvas;Lcom/android/systemui/newstatusbar/data/IconData;)V

    invoke-direct {p0, p1, v1}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->drawInternal(Landroid/graphics/Canvas;Lcom/android/systemui/newstatusbar/data/IconData;)V

    invoke-virtual {p1, v0}, Landroid/graphics/Canvas;->restoreToCount(I)V

    :goto_21
    return-void

    :cond_22
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/AnimatedImageView;->draw(Landroid/graphics/Canvas;)V

    goto :goto_21
.end method

.method public abstract getData()Lcom/android/systemui/newstatusbar/data/IconData;
.end method

.method protected abstract onAttached()V
.end method

.method public onAttachedToWindow()V
    .registers 1

    invoke-super {p0}, Lcom/android/systemui/statusbar/AnimatedImageView;->onAttachedToWindow()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->onAttached()V

    return-void
.end method

.method protected abstract onDetached()V
.end method

.method public onDetachedFromWindow()V
    .registers 1

    invoke-super {p0}, Lcom/android/systemui/statusbar/AnimatedImageView;->onDetachedFromWindow()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->onDetached()V

    return-void
.end method

.method public setColorFilter(Landroid/graphics/ColorFilter;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->colorFilter:Landroid/graphics/ColorFilter;

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/AnimatedImageView;->setColorFilter(Landroid/graphics/ColorFilter;)V

    return-void
.end method

.method public setImageDrawable(Landroid/graphics/drawable/Drawable;)V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isCustColor:Z

    if-eqz v0, :cond_13

    if-eqz p1, :cond_13

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isIconAdded:Z

    if-nez v0, :cond_13

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->updateSizeRatio(Landroid/graphics/drawable/Drawable;)V

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isIconAdded:Z

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->update()V

    :cond_13
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/AnimatedImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    return-void
.end method

.method public setImageResource(I)V
    .registers 5
    .annotation build Landroid/annotation/SuppressLint;
        value = {
            "UseCompatLoadingForDrawables"
        }
    .end annotation

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isCustColor:Z

    if-eqz v1, :cond_25

    if-eqz p1, :cond_25

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isIconAdded:Z

    if-nez v1, :cond_25

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->getContext()Landroid/content/Context;

    move-result-object v2

    invoke-virtual {v2}, Landroid/content/Context;->getTheme()Landroid/content/res/Resources$Theme;

    move-result-object v2

    invoke-virtual {v1, p1, v2}, Landroid/content/res/Resources;->getDrawable(ILandroid/content/res/Resources$Theme;)Landroid/graphics/drawable/Drawable;

    move-result-object v0

    if-eqz v0, :cond_25

    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->updateSizeRatio(Landroid/graphics/drawable/Drawable;)V

    const/4 v1, 0x1

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isIconAdded:Z

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->update()V

    :cond_25
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/AnimatedImageView;->setImageResource(I)V

    return-void
.end method

.method public setImageTintList(Landroid/content/res/ColorStateList;)V
    .registers 2
    .param p1  # Landroid/content/res/ColorStateList;
        .annotation build Landroidx/annotation/Nullable;
        .end annotation
    .end param

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->tint:Landroid/content/res/ColorStateList;

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/AnimatedImageView;->setImageTintList(Landroid/content/res/ColorStateList;)V

    return-void
.end method

.method public setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V
    .registers 6

    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isCustColor:Z

    if-eqz v2, :cond_32

    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isNeedZoom:Z

    if-eqz v2, :cond_32

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->getData()Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isIconAdded:Z

    if-eqz v2, :cond_32

    if-eqz v0, :cond_32

    if-eqz p1, :cond_32

    iget v1, v0, Lcom/android/systemui/newstatusbar/data/IconData;->zoom:I

    int-to-float v2, v1

    iget v3, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->mIconSize:I

    int-to-float v3, v3

    mul-float/2addr v2, v3

    const/high16 v3, 0x42c80000  # 100.0f

    div-float/2addr v2, v3

    float-to-int v2, v2

    iput v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->curHeight:I

    iget v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->curHeight:I

    int-to-float v2, v2

    iget v3, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->sizeRatio:F

    mul-float/2addr v2, v3

    float-to-int v2, v2

    iput v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->curWidth:I

    iget v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->curWidth:I

    iput v2, p1, Landroid/view/ViewGroup$LayoutParams;->width:I

    iget v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->curHeight:I

    iput v2, p1, Landroid/view/ViewGroup$LayoutParams;->height:I

    :cond_32
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/AnimatedImageView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    return-void
.end method

.method public setScaleType(Landroid/widget/ImageView$ScaleType;)V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isCustColor:Z

    if-nez v0, :cond_7

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/AnimatedImageView;->setScaleType(Landroid/widget/ImageView$ScaleType;)V

    :cond_7
    return-void
.end method

.method public update()V
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isIconAdded:Z

    if-eqz v0, :cond_e

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->isCustColor:Z

    if-eqz v0, :cond_e

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->updateZoom()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;->invalidate()V

    :cond_e
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_ext_ExtIconAnimated',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
