"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/ext/ExtTextView.smali'
CLASS_FALLBACK_NAMES = ['ExtTextView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public abstract Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;
.super Landroid/widget/TextView;


# instance fields
.field private isAttach:Z

.field protected isCustColor:Z

.field private mColorSet:I

.field private paint:Landroid/graphics/Paint;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 4

    invoke-direct {p0, p1}, Landroid/widget/TextView;-><init>(Landroid/content/Context;)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "use_config_color_size_element"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->BoolToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    const/4 v1, 0x1

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isCustColor:Z

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 5

    invoke-direct {p0, p1, p2}, Landroid/widget/TextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "use_config_color_size_element"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->BoolToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    const/4 v1, 0x1

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isCustColor:Z

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 6

    invoke-direct {p0, p1, p2, p3}, Landroid/widget/TextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "use_config_color_size_element"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->BoolToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    const/4 v1, 0x1

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isCustColor:Z

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V
    .registers 7

    invoke-direct {p0, p1, p2, p3, p4}, Landroid/widget/TextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "use_config_color_size_element"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->BoolToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    const/4 v1, 0x1

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isCustColor:Z

    return-void
.end method

.method private getTypeFace(Ljava/lang/String;)Landroid/graphics/Typeface;
    .registers 6

    const/4 v0, 0x0

    :try_start_1
    invoke-static {p1}, Landroid/graphics/Typeface;->createFromFile(Ljava/lang/String;)Landroid/graphics/Typeface;

    move-result-object v1
    :try_end_5
    .catch Ljava/lang/RuntimeException; {:try_start_1 .. :try_end_5} :catch_7

    move-object v0, v1

    goto :goto_15

    :catch_7
    move-exception v1

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v2

    const-string v3, "getTypeFase : fonts not found"

    invoke-static {v2, v3}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :goto_15
    return-object v0
.end method

.method private updateDefault()V
    .registers 4

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    if-eqz v0, :cond_23

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getCurrentTextColor()I

    move-result v1

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->defColor:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getTextSize()F

    move-result v1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    invoke-virtual {v2}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v2

    iget v2, v2, Landroid/util/DisplayMetrics;->scaledDensity:F

    div-float/2addr v1, v2

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->defSize:F

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getTypeface()Landroid/graphics/Typeface;

    move-result-object v1

    iput-object v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->defTypefase:Landroid/graphics/Typeface;

    :cond_23
    return-void
.end method

.method private updateTyperface()V
    .registers 5

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getPaint()Landroid/text/TextPaint;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->paint:Landroid/graphics/Paint;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    if-eqz v0, :cond_20

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/TextData;->getTypeFace()Landroid/graphics/Typeface;

    move-result-object v1

    iget v2, v0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFaseStyle:I

    invoke-super {p0, v1, v2}, Landroid/widget/TextView;->setTypeface(Landroid/graphics/Typeface;I)V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->paint:Landroid/graphics/Paint;

    iget v3, v0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFaseStyle:I

    invoke-static {v1, v3}, Landroid/graphics/Typeface;->create(Landroid/graphics/Typeface;I)Landroid/graphics/Typeface;

    move-result-object v3

    invoke-virtual {v2, v3}, Landroid/graphics/Paint;->setTypeface(Landroid/graphics/Typeface;)Landroid/graphics/Typeface;

    :cond_20
    return-void
.end method


# virtual methods
.method protected abstract getData()Lcom/android/systemui/newstatusbar/data/TextData;
.end method

.method protected abstract onAttached()V
.end method

.method protected onAttachedToWindow()V
    .registers 2

    goto/32 :goto_b

    nop

    :goto_4
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->post(Ljava/lang/Runnable;)Z

    goto/32 :goto_2e

    nop

    :goto_b
    invoke-super {p0}, Landroid/widget/TextView;->onAttachedToWindow()V

    goto/32 :goto_28

    nop

    :goto_12
    invoke-direct {v0, p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView$1;-><init>(Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;)V

    goto/32 :goto_4

    nop

    :goto_19
    if-eqz v0, :cond_1e

    goto/32 :goto_32

    :cond_1e
    goto/32 :goto_36

    nop

    :goto_22
    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isAttach:Z

    goto/32 :goto_2f

    nop

    :goto_28
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isAttach:Z

    goto/32 :goto_19

    nop

    :goto_2e
    return-void

    :goto_2f
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->updateDefault()V

    :goto_32
    goto/32 :goto_41

    nop

    :goto_36
    const/4 v0, 0x1

    goto/32 :goto_22

    nop

    :goto_3b
    new-instance v0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView$1;

    goto/32 :goto_12

    nop

    :goto_41
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->onAttached()V

    goto/32 :goto_3b

    nop
.end method

.method protected abstract onDetached()V
.end method

.method protected onDetachedFromWindow()V
    .registers 1

    goto/32 :goto_4

    nop

    :goto_4
    invoke-super {p0}, Landroid/widget/TextView;->onDetachedFromWindow()V

    goto/32 :goto_c

    nop

    :goto_b
    return-void

    :goto_c
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->onDetached()V

    goto/32 :goto_b

    nop
.end method

.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 8

    goto/32 :goto_38

    nop

    :goto_4
    invoke-super {p0, p1}, Landroid/widget/TextView;->onDraw(Landroid/graphics/Canvas;)V

    goto/32 :goto_f0

    nop

    :goto_b
    if-eqz v0, :cond_10

    goto/32 :goto_40

    :cond_10
    goto/32 :goto_c3

    nop

    :goto_14
    int-to-float v4, v4

    goto/32 :goto_19

    nop

    :goto_19
    iget-object v5, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->paint:Landroid/graphics/Paint;

    goto/32 :goto_88

    nop

    :goto_1f
    int-to-float v1, v1

    goto/32 :goto_24

    nop

    :goto_24
    const/high16 v2, 0x41200000  # 10.0f

    goto/32 :goto_d3

    nop

    :goto_2a
    sub-float/2addr v2, v3

    goto/32 :goto_6f

    nop

    :goto_2f
    if-nez v0, :cond_34

    goto/32 :goto_90

    :cond_34
    goto/32 :goto_a8

    nop

    :goto_38
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isCustColor:Z

    goto/32 :goto_2f

    nop

    :goto_3e
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->paint:Landroid/graphics/Paint;

    :goto_40
    goto/32 :goto_e3

    nop

    :goto_44
    if-eqz v2, :cond_49

    goto/32 :goto_56

    :cond_49
    goto/32 :goto_94

    nop

    :goto_4d
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getHeight()I

    move-result v2

    goto/32 :goto_d8

    nop

    :goto_55
    goto :goto_6b

    :goto_56
    goto/32 :goto_67

    nop

    :goto_5a
    div-float/2addr v3, v1

    goto/32 :goto_2a

    nop

    :goto_5f
    invoke-interface {v3}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v3

    goto/32 :goto_a0

    nop

    :goto_67
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/TextData;->getColor()I

    move-result v2

    :goto_6b
    goto/32 :goto_bc

    nop

    :goto_6f
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getText()Ljava/lang/CharSequence;

    move-result-object v3

    goto/32 :goto_5f

    nop

    :goto_77
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->paint:Landroid/graphics/Paint;

    goto/32 :goto_b4

    nop

    :goto_7d
    div-float/2addr v2, v3

    goto/32 :goto_ae

    nop

    :goto_82
    iget v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->division:I

    goto/32 :goto_1f

    nop

    :goto_88
    invoke-virtual {p1, v3, v4, v2, v5}, Landroid/graphics/Canvas;->drawText(Ljava/lang/String;FFLandroid/graphics/Paint;)V

    goto/32 :goto_8f

    nop

    :goto_8f
    return-void

    :goto_90
    goto/32 :goto_4

    nop

    :goto_94
    iget v2, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->mColorSet:I

    goto/32 :goto_55

    nop

    :goto_9a
    iget v2, v0, Lcom/android/systemui/newstatusbar/data/TextData;->color:I

    goto/32 :goto_44

    nop

    :goto_a0
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getPaddingStart()I

    move-result v4

    goto/32 :goto_14

    nop

    :goto_a8
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->paint:Landroid/graphics/Paint;

    goto/32 :goto_b

    nop

    :goto_ae
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->paint:Landroid/graphics/Paint;

    goto/32 :goto_cb

    nop

    :goto_b4
    invoke-virtual {v4}, Landroid/graphics/Paint;->ascent()F

    move-result v4

    goto/32 :goto_eb

    nop

    :goto_bc
    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setColor(I)V

    goto/32 :goto_82

    nop

    :goto_c3
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getPaint()Landroid/text/TextPaint;

    move-result-object v0

    goto/32 :goto_3e

    nop

    :goto_cb
    invoke-virtual {v3}, Landroid/graphics/Paint;->descent()F

    move-result v3

    goto/32 :goto_77

    nop

    :goto_d3
    div-float/2addr v1, v2

    goto/32 :goto_4d

    nop

    :goto_d8
    int-to-float v2, v2

    goto/32 :goto_dd

    nop

    :goto_dd
    const/high16 v3, 0x40000000  # 2.0f

    goto/32 :goto_7d

    nop

    :goto_e3
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    goto/32 :goto_f1

    nop

    :goto_eb
    add-float/2addr v3, v4

    goto/32 :goto_5a

    nop

    :goto_f0
    return-void

    :goto_f1
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->paint:Landroid/graphics/Paint;

    goto/32 :goto_9a

    nop
.end method

.method protected onMeasure(II)V
    .registers 6

    goto/32 :goto_4f

    nop

    :goto_4
    invoke-virtual {p0, v0, v1}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->setMeasuredDimension(II)V

    :goto_7
    goto/32 :goto_7c

    nop

    :goto_b
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isCustColor:Z

    goto/32 :goto_38

    nop

    :goto_11
    add-int/2addr v0, v1

    goto/32 :goto_1e

    nop

    :goto_16
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getMeasuredHeight()I

    move-result v1

    goto/32 :goto_4

    nop

    :goto_1e
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v1

    goto/32 :goto_76

    nop

    :goto_26
    const/4 v2, 0x0

    :goto_27
    goto/32 :goto_30

    nop

    :goto_2b
    const/4 v2, 0x1

    goto/32 :goto_63

    nop

    :goto_30
    invoke-static {p0, v2}, Lcom/android/systemui/newstatusbar/util/TextUtil;->measureText(Landroid/widget/TextView;Z)I

    move-result v1

    goto/32 :goto_71

    nop

    :goto_38
    if-nez v0, :cond_3d

    goto/32 :goto_7

    :cond_3d
    nop

    goto/32 :goto_47

    nop

    :goto_42
    goto :goto_27

    :goto_43
    goto/32 :goto_26

    nop

    :goto_47
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getPaddingRight()I

    move-result v0

    goto/32 :goto_7d

    nop

    :goto_4f
    invoke-super {p0, p1, p2}, Landroid/widget/TextView;->onMeasure(II)V

    goto/32 :goto_b

    nop

    :goto_56
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getPaddingEnd()I

    move-result v1

    goto/32 :goto_11

    nop

    :goto_5e
    add-int/2addr v0, v1

    goto/32 :goto_85

    nop

    :goto_63
    if-gt v1, v2, :cond_68

    goto/32 :goto_43

    :cond_68
    goto/32 :goto_42

    nop

    :goto_6c
    add-int/2addr v0, v1

    goto/32 :goto_56

    nop

    :goto_71
    add-int/2addr v0, v1

    goto/32 :goto_16

    nop

    :goto_76
    iget v1, v1, Lcom/android/systemui/newstatusbar/data/TextData;->typeFaseStyle:I

    goto/32 :goto_2b

    nop

    :goto_7c
    return-void

    :goto_7d
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getPaddingStart()I

    move-result v1

    goto/32 :goto_5e

    nop

    :goto_85
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getPaddingLeft()I

    move-result v1

    goto/32 :goto_6c

    nop
.end method

.method public setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/widget/TextView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isCustColor:Z

    if-eqz v0, :cond_b

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->setTextSize(F)V

    :cond_b
    return-void
.end method

.method public setTextAppearance(I)V
    .registers 2

    invoke-super {p0, p1}, Landroid/widget/TextView;->setTextAppearance(I)V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->updateDefault()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->update()V

    return-void
.end method

.method public setTextColor()V
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isCustColor:Z

    if-eqz v0, :cond_b

    const/4 v0, 0x0

    invoke-super {p0, v0}, Landroid/widget/TextView;->setTextColor(I)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->invalidate()V

    :cond_b
    return-void
.end method

.method public setTextColor(I)V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isCustColor:Z

    if-nez v0, :cond_8

    invoke-super {p0, p1}, Landroid/widget/TextView;->setTextColor(I)V

    return-void

    :cond_8
    const/4 v0, 0x0

    invoke-super {p0, v0}, Landroid/widget/TextView;->setTextColor(I)V

    if-eqz p1, :cond_10

    iput p1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->mColorSet:I

    :cond_10
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->setTextColor()V

    return-void
.end method

.method public setTextColor(Landroid/content/res/ColorStateList;)V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isCustColor:Z

    if-nez v0, :cond_8

    invoke-super {p0, p1}, Landroid/widget/TextView;->setTextColor(Landroid/content/res/ColorStateList;)V

    return-void

    :cond_8
    const/4 v0, 0x0

    invoke-static {v0}, Landroid/content/res/ColorStateList;->valueOf(I)Landroid/content/res/ColorStateList;

    move-result-object v0

    invoke-super {p0, v0}, Landroid/widget/TextView;->setTextColor(Landroid/content/res/ColorStateList;)V

    invoke-virtual {p1}, Landroid/content/res/ColorStateList;->getDefaultColor()I

    move-result v0

    if-eqz v0, :cond_18

    iput v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->mColorSet:I

    :cond_18
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->setTextColor()V

    return-void
.end method

.method public setTextSize(F)V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isCustColor:Z

    if-eqz v0, :cond_d

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/TextData;->getSize()F

    move-result v0

    goto :goto_e

    :cond_d
    move v0, p1

    :goto_e
    invoke-super {p0, v0}, Landroid/widget/TextView;->setTextSize(F)V

    return-void
.end method

.method public setTextSize(IF)V
    .registers 5

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isCustColor:Z

    if-nez v0, :cond_8

    invoke-super {p0, p1, p2}, Landroid/widget/TextView;->setTextSize(IF)V

    return-void

    :cond_8
    const/4 v0, 0x2

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v1

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/data/TextData;->getSize()F

    move-result v1

    invoke-super {p0, v0, v1}, Landroid/widget/TextView;->setTextSize(IF)V

    return-void
.end method

.method public setTypeface(Landroid/graphics/Typeface;)V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isCustColor:Z

    if-nez v0, :cond_7

    invoke-super {p0, p1}, Landroid/widget/TextView;->setTypeface(Landroid/graphics/Typeface;)V

    :cond_7
    return-void
.end method

.method public setTypeface(Landroid/graphics/Typeface;I)V
    .registers 4

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isCustColor:Z

    if-nez v0, :cond_7

    invoke-super {p0, p1, p2}, Landroid/widget/TextView;->setTypeface(Landroid/graphics/Typeface;I)V

    :cond_7
    return-void
.end method

.method public update()V
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->isCustColor:Z

    if-eqz v0, :cond_11

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->setTextColor()V

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->setTextSize(F)V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->updateTyperface()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->invalidate()V

    :cond_11
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_ext_ExtTextView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
