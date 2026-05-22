"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView.smali'
CLASS_FALLBACK_NAMES = ['ClockLayout$CenterTextView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;
.super Landroid/widget/TextView;

# interfaces
.implements Lcom/android/systemui/newstatusbar/clock/IClock;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/clock/ClockLayout;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x2
    name = "CenterTextView"
.end annotation


# instance fields
.field private final DEFAULT_ROTATE_CAMERA_DISTANCE:F

.field private animator:Landroid/animation/ObjectAnimator;

.field private interpolator:Landroid/animation/TimeInterpolator;

.field isDot:Z

.field public mActive:Z

.field private mWidth:F

.field private final rect:I

.field private final rotateToX:I

.field private final rotateToY:I

.field private text:Ljava/lang/String;

.field final synthetic this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

.field private final tmpRect:Landroid/graphics/Rect;

.field private final translateDown:I

.field private final translateLeft:I


# direct methods
.method public constructor <init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout;Landroid/content/Context;)V
    .registers 7

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    invoke-direct {p0, p2}, Landroid/widget/TextView;-><init>(Landroid/content/Context;)V

    const/4 p1, 0x1

    iput-boolean p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->mActive:Z

    iput p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->translateDown:I

    const/4 p1, 0x2

    iput p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->translateLeft:I

    const/4 p1, 0x3

    iput p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->rotateToX:I

    const/4 p1, 0x4

    iput p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->rotateToY:I

    const/4 p1, 0x5

    iput p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->rect:I

    const/4 p1, 0x0

    iput-boolean p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->isDot:Z

    new-instance p1, Landroid/graphics/Rect;

    invoke-direct {p1}, Landroid/graphics/Rect;-><init>()V

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->tmpRect:Landroid/graphics/Rect;

    const-string p1, ""

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->text:Ljava/lang/String;

    new-instance p1, Landroid/view/animation/AccelerateInterpolator;

    const v0, 0x3f666666  # 0.9f

    invoke-direct {p1, v0}, Landroid/view/animation/AccelerateInterpolator;-><init>(F)V

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->interpolator:Landroid/animation/TimeInterpolator;

    invoke-static {}, Landroid/content/res/Resources;->getSystem()Landroid/content/res/Resources;

    move-result-object p1

    invoke-virtual {p1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object p1

    iget v0, p1, Landroid/util/DisplayMetrics;->density:F

    float-to-double v0, v0

    const-wide/high16 v2, 0x4000000000000000L  # 2.0

    invoke-static {v2, v3, v0, v1}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v0

    iget v2, p1, Landroid/util/DisplayMetrics;->heightPixels:I

    int-to-double v2, v2

    mul-double/2addr v0, v2

    iget v2, p1, Landroid/util/DisplayMetrics;->density:F

    float-to-double v2, v2

    div-double/2addr v0, v2

    const-wide/high16 v2, 0x4074000000000000L  # 320.0

    div-double/2addr v0, v2

    const-wide/high16 v2, 0x4094000000000000L  # 1280.0

    mul-double/2addr v0, v2

    double-to-float v0, v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->DEFAULT_ROTATE_CAMERA_DISTANCE:F

    return-void
.end method

.method static synthetic access$100(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;)F
    .registers 2

    iget v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->DEFAULT_ROTATE_CAMERA_DISTANCE:F

    return v0
.end method

.method static synthetic access$200(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->gotoInitialState()V

    return-void
.end method

.method private gotoInitialState()V
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->mActive:Z

    xor-int/lit8 v0, v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->mActive:Z

    if-eqz v0, :cond_a

    const/4 v0, 0x0

    goto :goto_b

    :cond_a
    const/4 v0, 0x4

    :goto_b
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setVisibility(I)V

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setRotationX(F)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setRotationY(F)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setX(F)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setY(F)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setPivotX(F)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setPivotY(F)V

    return-void
.end method

.method private startAnimView()V
    .registers 12

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->getTextHeight()F

    move-result v0

    iget v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->mWidth:F

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    iget-object v2, v2, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v2

    iget v2, v2, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->animStyle:I

    const/4 v3, 0x0

    const/4 v4, 0x1

    const/4 v5, 0x2

    const/4 v6, 0x0

    if-eq v2, v4, :cond_97

    if-eq v2, v5, :cond_76

    const/4 v7, 0x3

    const/high16 v8, 0x40000000  # 2.0f

    const/high16 v9, 0x42b40000  # 90.0f

    if-eq v2, v7, :cond_54

    const/4 v7, 0x4

    if-eq v2, v7, :cond_31

    sget-object v4, Landroid/view/View;->ALPHA:Landroid/util/Property;

    new-array v5, v5, [F

    fill-array-data v5, :array_d8

    invoke-static {p0, v4, v5}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Landroid/util/Property;[F)Landroid/animation/ObjectAnimator;

    move-result-object v4

    iput-object v4, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->animator:Landroid/animation/ObjectAnimator;

    goto/16 :goto_b8

    :cond_31
    iget-boolean v7, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->mActive:Z

    if-eqz v7, :cond_37

    move v7, v6

    goto :goto_38

    :cond_37
    move v7, v9

    :goto_38
    sget-object v10, Landroid/view/View;->ROTATION_Y:Landroid/util/Property;

    new-array v5, v5, [F

    sub-float/2addr v6, v7

    aput v6, v5, v3

    sub-float/2addr v9, v7

    aput v9, v5, v4

    invoke-static {p0, v10, v5}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Landroid/util/Property;[F)Landroid/animation/ObjectAnimator;

    move-result-object v4

    iput-object v4, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->animator:Landroid/animation/ObjectAnimator;

    div-float v4, v1, v8

    invoke-virtual {p0, v4}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setPivotX(F)V

    div-float v4, v0, v8

    invoke-virtual {p0, v4}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setPivotY(F)V

    goto/16 :goto_b8

    :cond_54
    iget-boolean v7, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->mActive:Z

    if-eqz v7, :cond_5a

    move v7, v6

    goto :goto_5b

    :cond_5a
    move v7, v9

    :goto_5b
    sget-object v10, Landroid/view/View;->ROTATION_X:Landroid/util/Property;

    new-array v5, v5, [F

    sub-float/2addr v6, v7

    aput v6, v5, v3

    sub-float/2addr v9, v7

    aput v9, v5, v4

    invoke-static {p0, v10, v5}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Landroid/util/Property;[F)Landroid/animation/ObjectAnimator;

    move-result-object v4

    iput-object v4, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->animator:Landroid/animation/ObjectAnimator;

    div-float v4, v1, v8

    invoke-virtual {p0, v4}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setPivotX(F)V

    div-float v4, v0, v8

    invoke-virtual {p0, v4}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setPivotY(F)V

    goto :goto_b8

    :cond_76
    iget-boolean v7, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->mActive:Z

    if-eqz v7, :cond_7c

    move v7, v6

    goto :goto_7d

    :cond_7c
    move v7, v1

    :goto_7d
    sget-object v8, Landroid/view/View;->TRANSLATION_X:Landroid/util/Property;

    new-array v5, v5, [F

    sub-float/2addr v6, v7

    aput v6, v5, v3

    sub-float v6, v1, v7

    aput v6, v5, v4

    invoke-static {p0, v8, v5}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Landroid/util/Property;[F)Landroid/animation/ObjectAnimator;

    move-result-object v4

    iput-object v4, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->animator:Landroid/animation/ObjectAnimator;

    new-instance v5, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$3;

    invoke-direct {v5, p0, v1, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$3;-><init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;FF)V

    invoke-virtual {v4, v5}, Landroid/animation/ObjectAnimator;->addUpdateListener(Landroid/animation/ValueAnimator$AnimatorUpdateListener;)V

    goto :goto_b8

    :cond_97
    iget-boolean v7, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->mActive:Z

    if-eqz v7, :cond_9d

    move v7, v6

    goto :goto_9e

    :cond_9d
    move v7, v0

    :goto_9e
    sget-object v8, Landroid/view/View;->TRANSLATION_Y:Landroid/util/Property;

    new-array v5, v5, [F

    sub-float/2addr v6, v7

    aput v6, v5, v3

    sub-float v6, v0, v7

    aput v6, v5, v4

    invoke-static {p0, v8, v5}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Landroid/util/Property;[F)Landroid/animation/ObjectAnimator;

    move-result-object v4

    iput-object v4, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->animator:Landroid/animation/ObjectAnimator;

    new-instance v5, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$2;

    invoke-direct {v5, p0, v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$2;-><init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;FF)V

    invoke-virtual {v4, v5}, Landroid/animation/ObjectAnimator;->addUpdateListener(Landroid/animation/ValueAnimator$AnimatorUpdateListener;)V

    nop

    :goto_b8
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->animator:Landroid/animation/ObjectAnimator;

    if-lez v2, :cond_bf

    const-wide/16 v5, 0x12c

    goto :goto_c1

    :cond_bf
    const-wide/16 v5, 0x0

    :goto_c1
    invoke-virtual {v4, v5, v6}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->animator:Landroid/animation/ObjectAnimator;

    new-instance v5, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$4;

    invoke-direct {v5, p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$4;-><init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;)V

    invoke-virtual {v4, v5}, Landroid/animation/ObjectAnimator;->addListener(Landroid/animation/Animator$AnimatorListener;)V

    invoke-virtual {p0, v3}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setVisibility(I)V

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->animator:Landroid/animation/ObjectAnimator;

    invoke-virtual {v3}, Landroid/animation/ObjectAnimator;->start()V

    return-void

    nop

    :array_d8
    .array-data 4
        0x3f800000  # 1.0f
        0x3f800000  # 1.0f
    .end array-data
.end method


# virtual methods
.method public draw(Landroid/graphics/Canvas;)V
    .registers 11

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->getPaint()Landroid/text/TextPaint;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    iget-object v1, v1, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v1

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->getColor()I

    move-result v1

    invoke-virtual {v0, v1}, Landroid/text/TextPaint;->setColor(I)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->getText()Ljava/lang/String;

    move-result-object v2

    const-string v3, "0"

    invoke-virtual {v0, v3}, Landroid/text/TextPaint;->measureText(Ljava/lang/String;)F

    move-result v3

    iput v3, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->mWidth:F

    invoke-virtual {v0, v2}, Landroid/text/TextPaint;->measureText(Ljava/lang/String;)F

    move-result v4

    sub-float/2addr v3, v4

    const/high16 v4, 0x40000000  # 2.0f

    div-float/2addr v3, v4

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    iget-object v4, v4, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    invoke-virtual {v4}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v4

    iget v4, v4, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->division:I

    int-to-float v4, v4

    const/high16 v5, 0x41200000  # 10.0f

    div-float/2addr v4, v5

    const-string v5, "1"

    invoke-virtual {v2, v5}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v5

    if-eqz v5, :cond_3f

    move v5, v3

    goto :goto_40

    :cond_3f
    const/4 v5, 0x0

    :goto_40
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->getHeight()I

    move-result v6

    div-int/lit8 v6, v6, 0x2

    int-to-float v6, v6

    invoke-virtual {v0}, Landroid/text/TextPaint;->descent()F

    move-result v7

    invoke-virtual {v0}, Landroid/text/TextPaint;->ascent()F

    move-result v8

    add-float/2addr v7, v8

    div-float/2addr v7, v4

    sub-float/2addr v6, v7

    float-to-int v6, v6

    int-to-float v6, v6

    invoke-virtual {p1, v2, v5, v6, v0}, Landroid/graphics/Canvas;->drawText(Ljava/lang/String;FFLandroid/graphics/Paint;)V

    return-void
.end method

.method public fullInvalidate()V
    .registers 1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->invalidate()V

    return-void
.end method

.method public bridge synthetic getText()Ljava/lang/CharSequence;
    .registers 2

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->getText()Ljava/lang/String;

    move-result-object v0

    return-object v0
.end method

.method public getText()Ljava/lang/String;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->text:Ljava/lang/String;

    return-object v0
.end method

.method public getTextHeight()F
    .registers 6

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->getPaint()Landroid/text/TextPaint;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->tmpRect:Landroid/graphics/Rect;

    const-string v2, "0"

    const/4 v3, 0x0

    const/4 v4, 0x1

    invoke-virtual {v0, v2, v3, v4, v1}, Landroid/text/TextPaint;->getTextBounds(Ljava/lang/String;IILandroid/graphics/Rect;)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->tmpRect:Landroid/graphics/Rect;

    invoke-virtual {v0}, Landroid/graphics/Rect;->height()I

    move-result v0

    int-to-float v0, v0

    return v0
.end method

.method protected onMeasure(II)V
    .registers 6

    goto/32 :goto_c

    nop

    :goto_4
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->getTextHeight()F

    move-result v2

    goto/32 :goto_31

    nop

    :goto_c
    invoke-super {p0, p1, p2}, Landroid/widget/TextView;->onMeasure(II)V

    goto/32 :goto_44

    nop

    :goto_13
    float-to-int v1, v1

    goto/32 :goto_4

    nop

    :goto_18
    if-nez v0, :cond_1d

    goto/32 :goto_4b

    :cond_1d
    goto/32 :goto_4f

    nop

    :goto_21
    return-void

    :goto_22
    invoke-virtual {v1, v0}, Landroid/text/TextPaint;->measureText(Ljava/lang/String;)F

    move-result v1

    goto/32 :goto_13

    nop

    :goto_2a
    invoke-virtual {p0, v1, v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setMeasuredDimension(II)V

    goto/32 :goto_21

    nop

    :goto_31
    float-to-int v2, v2

    goto/32 :goto_2a

    nop

    :goto_36
    const-string v0, "0"

    :goto_38
    goto/32 :goto_3c

    nop

    :goto_3c
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->getPaint()Landroid/text/TextPaint;

    move-result-object v1

    goto/32 :goto_22

    nop

    :goto_44
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->isDot:Z

    goto/32 :goto_18

    nop

    :goto_4a
    goto :goto_38

    :goto_4b
    goto/32 :goto_36

    nop

    :goto_4f
    const-string v0, ":"

    goto/32 :goto_4a

    nop
.end method

.method public onTextChanged(Ljava/lang/CharSequence;)V
    .registers 2

    return-void
.end method

.method public requestLayout()V
    .registers 3

    const-string v0, "clock_app"

    const-string v1, "requestLayout: "

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    invoke-super {p0}, Landroid/widget/TextView;->requestLayout()V

    return-void
.end method

.method public setText(Ljava/lang/CharSequence;Landroid/widget/TextView$BufferType;)V
    .registers 4

    invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->text:Ljava/lang/String;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->invalidate()V

    return-void
.end method

.method public setText(Ljava/lang/String;Z)V
    .registers 6

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->animator:Landroid/animation/ObjectAnimator;

    if-eqz v0, :cond_1d

    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->isStarted()Z

    move-result v0

    if-eqz v0, :cond_1d

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->animator:Landroid/animation/ObjectAnimator;

    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->isRunning()Z

    move-result v0

    if-eqz v0, :cond_1d

    new-instance v0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1;

    invoke-direct {v0, p0, p1, p2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1;-><init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;Ljava/lang/String;Z)V

    const-wide/16 v1, 0x12c

    invoke-virtual {p0, v0, v1, v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->postDelayed(Ljava/lang/Runnable;J)Z

    return-void

    :cond_1d
    if-nez p2, :cond_23

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setText(Ljava/lang/CharSequence;)V

    goto :goto_39

    :cond_23
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->mActive:Z

    if-nez v0, :cond_2a

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setText(Ljava/lang/CharSequence;)V

    :cond_2a
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->getPaint()Landroid/text/TextPaint;

    move-result-object v0

    const-string v1, "0"

    invoke-virtual {v0, v1}, Landroid/text/TextPaint;->measureText(Ljava/lang/String;)F

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->mWidth:F

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->startAnimView()V

    :goto_39
    return-void
.end method

.method public setTextSizeWidthAnimation(F)V
    .registers 3

    const/4 v0, 0x0

    invoke-super {p0, v0, p1}, Landroid/widget/TextView;->setTextSize(IF)V

    return-void
.end method

.method public setVisibility(I)V
    .registers 3

    if-nez p1, :cond_5

    const/high16 v0, 0x3f800000  # 1.0f

    goto :goto_6

    :cond_5
    const/4 v0, 0x0

    :goto_6
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setAlpha(F)V

    return-void
.end method

.method public updateTypeface(Landroid/graphics/Typeface;I)V
    .registers 5

    invoke-virtual {p0, p1, p2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setTypeface(Landroid/graphics/Typeface;I)V

    invoke-static {p1, p2}, Landroid/graphics/Typeface;->create(Landroid/graphics/Typeface;I)Landroid/graphics/Typeface;

    move-result-object v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->getPaint()Landroid/text/TextPaint;

    move-result-object v1

    invoke-virtual {v1, v0}, Landroid/text/TextPaint;->setTypeface(Landroid/graphics/Typeface;)Landroid/graphics/Typeface;

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_clock_ClockLayout_CenterTextView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
