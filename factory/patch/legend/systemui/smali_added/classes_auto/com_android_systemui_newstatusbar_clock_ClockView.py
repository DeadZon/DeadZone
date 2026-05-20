"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/clock/ClockView.smali'
CLASS_FALLBACK_NAMES = ['ClockView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/clock/ClockView;
.super Lcom/android/systemui/statusbar/views/MiuiClock;

# interfaces
.implements Lcom/android/systemui/newstatusbar/policy/ISlots;


# instance fields
.field private clickListener:Landroid/view/View$OnClickListener;

.field private clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

.field isAttach:Z

.field private final key:Ljava/lang/String;

.field private slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

.field private text:Ljava/lang/String;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    const/4 v0, 0x0

    invoke-direct {p0, p1, v0}, Lcom/android/systemui/newstatusbar/clock/ClockView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    const/4 v0, 0x0

    invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/newstatusbar/clock/ClockView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 6

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/views/MiuiClock;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const-string v0, ""

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->text:Ljava/lang/String;

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->isAttach:Z

    const/4 v0, 0x0

    const-string v1, "settingsKey"

    invoke-interface {p2, v0, v1}, Landroid/util/AttributeSet;->getAttributeValue(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->key:Ljava/lang/String;

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/clock/ClockView;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->attachClockLayout()V

    return-void
.end method

.method private attachClockLayout()V
    .registers 8

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->isAttach:Z

    if-nez v0, :cond_69

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->isAttach:Z

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup;

    invoke-virtual {v0, p0}, Landroid/view/ViewGroup;->indexOfChild(Landroid/view/View;)I

    move-result v1

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->key:Ljava/lang/String;

    const-string v3, "expanded_clock"

    invoke-virtual {v3, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    invoke-static {p0, v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutFactory;->get(Lcom/android/systemui/newstatusbar/clock/ClockView;Z)Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    move-result-object v2

    iput-object v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    new-instance v4, Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    iget-object v5, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    iget-object v6, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->key:Ljava/lang/String;

    invoke-direct {v4, v5, v6}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;-><init>(Lcom/android/systemui/newstatusbar/clock/IClock;Ljava/lang/String;)V

    iput-object v4, v2, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    iget-object v2, v2, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->register()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->updateDefault()V

    invoke-virtual {v0, p0}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    new-instance v4, Landroid/view/ViewGroup$LayoutParams;

    const/4 v5, -0x2

    invoke-direct {v4, v5, v5}, Landroid/view/ViewGroup$LayoutParams;-><init>(II)V

    invoke-virtual {v2, p0, v4}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->initialize()V

    new-instance v2, Landroid/widget/LinearLayout$LayoutParams;

    invoke-direct {v2, v5, v5}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V

    const/16 v4, 0x10

    iput v4, v2, Landroid/widget/LinearLayout$LayoutParams;->gravity:I

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->key:Ljava/lang/String;

    invoke-virtual {v3, v4}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v3

    if-eqz v3, :cond_5c

    const/16 v3, 0x14

    iput v3, v2, Landroid/widget/LinearLayout$LayoutParams;->rightMargin:I

    :cond_5c
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    invoke-virtual {v0, v3, v1, v2}, Landroid/view/ViewGroup;->addView(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->updateTime()V

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    invoke-virtual {v3}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->requestLayout()V

    :cond_69
    return-void
.end method

.method private deleteZero(Ljava/lang/String;)Ljava/lang/String;
    .registers 3

    invoke-virtual {p1}, Ljava/lang/String;->isEmpty()Z

    move-result v0

    if-nez v0, :cond_13

    const-string v0, "0"

    invoke-virtual {p1, v0}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result v0

    if-nez v0, :cond_13

    const/4 v0, 0x1

    invoke-virtual {p1, v0}, Ljava/lang/String;->substring(I)Ljava/lang/String;

    move-result-object p1

    :cond_13
    return-object p1
.end method

.method private updateDefault()V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_29

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getClockSettings()Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getCurrentTextColor()I

    move-result v1

    iput v1, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->defColor:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getTextSize()F

    move-result v1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    invoke-virtual {v2}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v2

    iget v2, v2, Landroid/util/DisplayMetrics;->scaledDensity:F

    div-float/2addr v1, v2

    iput v1, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->defSize:F

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getTypeface()Landroid/graphics/Typeface;

    move-result-object v1

    iput-object v1, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->defTypefase:Landroid/graphics/Typeface;

    :cond_29
    return-void
.end method


# virtual methods
.method public addOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_7

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->addOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    :cond_7
    return-void
.end method

.method public animate()Landroid/view/ViewPropertyAnimator;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_9

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    return-object v0

    :cond_9
    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiClock;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    return-object v0
.end method

.method public draw(Landroid/graphics/Canvas;)V
    .registers 2

    return-void
.end method

.method public getAlpha()F
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_9

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getAlpha()F

    move-result v0

    return v0

    :cond_9
    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiClock;->getAlpha()F

    move-result v0

    return v0
.end method

.method public getLocationInSurface([I)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_8

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getLocationInSurface([I)V

    return-void

    :cond_8
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->getLocationInSurface([I)V

    return-void
.end method

.method public getLocationInWindow([I)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_8

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getLocationInWindow([I)V

    return-void

    :cond_8
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->getLocationInWindow([I)V

    return-void
.end method

.method public getLocationOnScreen([I)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_8

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getLocationOnScreen([I)V

    return-void

    :cond_8
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->getLocationOnScreen([I)V

    return-void
.end method

.method public bridge synthetic getText()Ljava/lang/CharSequence;
    .registers 2

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getText()Ljava/lang/String;

    move-result-object v0

    return-object v0
.end method

.method public getText()Ljava/lang/String;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->text:Ljava/lang/String;

    return-object v0
.end method

.method public getTransitionAlpha()F
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_9

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getTransitionAlpha()F

    move-result v0

    return v0

    :cond_9
    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiClock;->getTransitionAlpha()F

    move-result v0

    return v0
.end method

.method public getTranslationX()F
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_9

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getTranslationX()F

    move-result v0

    return v0

    :cond_9
    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiClock;->getTranslationX()F

    move-result v0

    return v0
.end method

.method public getTranslationY()F
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_9

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getTranslationY()F

    move-result v0

    return v0

    :cond_9
    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiClock;->getTranslationY()F

    move-result v0

    return v0
.end method

.method public onAttachedToWindow()V
    .registers 2

    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiClock;->onAttachedToWindow()V

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->isAttach:Z

    if-nez v0, :cond_f

    new-instance v0, Lcom/android/systemui/newstatusbar/clock/ClockView$1;

    invoke-direct {v0, p0}, Lcom/android/systemui/newstatusbar/clock/ClockView$1;-><init>(Lcom/android/systemui/newstatusbar/clock/ClockView;)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->post(Ljava/lang/Runnable;)Z

    :cond_f
    return-void
.end method

.method protected onMeasure(II)V
    .registers 5

    goto/32 :goto_12

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    goto/32 :goto_1f

    nop

    :goto_a
    return-void

    :goto_b
    invoke-virtual {p0, v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockView;->setMeasuredDimension(II)V

    :goto_e
    goto/32 :goto_a

    nop

    :goto_12
    invoke-super {p0, p1, p2}, Lcom/android/systemui/statusbar/views/MiuiClock;->onMeasure(II)V

    goto/32 :goto_4

    nop

    :goto_19
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    goto/32 :goto_28

    nop

    :goto_1f
    if-nez v0, :cond_24

    goto/32 :goto_e

    :cond_24
    goto/32 :goto_30

    nop

    :goto_28
    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getMeasuredHeight()I

    move-result v1

    goto/32 :goto_b

    nop

    :goto_30
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getMeasuredWidth()I

    move-result v0

    goto/32 :goto_19

    nop
.end method

.method protected onTextChanged(Ljava/lang/CharSequence;III)V
    .registers 6

    goto/32 :goto_e

    nop

    :goto_4
    if-nez v0, :cond_9

    goto/32 :goto_17

    :cond_9
    goto/32 :goto_14

    nop

    :goto_d
    return-void

    :goto_e
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    goto/32 :goto_4

    nop

    :goto_14
    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->onTextChanged(Ljava/lang/CharSequence;)V

    :goto_17
    goto/32 :goto_d

    nop
.end method

.method public removeOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_7

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->removeOnLayoutChangeListener(Landroid/view/View$OnLayoutChangeListener;)V

    :cond_7
    return-void
.end method

.method public setAlpha(F)V
    .registers 3

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->setAlpha(F)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_a

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->setAlpha(F)V

    :cond_a
    return-void
.end method

.method public setPolicyVisibility(I)V
    .registers 2

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->setPolicyVisibility(I)V

    return-void
.end method

.method public setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V
    .registers 3

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->mMiuiStatusBarClockController:Lcom/android/systemui/statusbar/policy/MiuiStatusBarClockController;

    iget-object v0, v0, Lcom/android/systemui/statusbar/policy/MiuiStatusBarClockController;->mDarkIconDispatcher:Lcom/android/systemui/plugins/DarkIconDispatcher;

    invoke-interface {v0}, Lcom/android/systemui/plugins/DarkIconDispatcher;->reapply()V

    return-void
.end method

.method public setText(Ljava/lang/CharSequence;Landroid/widget/TextView$BufferType;)V
    .registers 4

    invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->text:Ljava/lang/String;

    const/4 v0, 0x0

    invoke-virtual {p0, p1, v0, v0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->onTextChanged(Ljava/lang/CharSequence;III)V

    return-void
.end method

.method public setTextAppearance(I)V
    .registers 3

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->setTextAppearance(I)V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->updateDefault()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_d

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->fullInvalidate()V

    :cond_d
    return-void
.end method

.method public setTextColor(I)V
    .registers 3

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->setTextColor(I)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_16

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getClockSettings()Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v0

    iput p1, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->defColor:I

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->fullInvalidate()V

    :cond_16
    return-void
.end method

.method public setTextColor(Landroid/content/res/ColorStateList;)V
    .registers 4

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->setTextColor(Landroid/content/res/ColorStateList;)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_1a

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getClockSettings()Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getCurrentTextColor()I

    move-result v1

    iput v1, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->defColor:I

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->fullInvalidate()V

    :cond_1a
    return-void
.end method

.method public setTextSize(F)V
    .registers 5

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->setTextSize(F)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_25

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getClockSettings()Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getTextSize()F

    move-result v1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    invoke-virtual {v2}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v2

    iget v2, v2, Landroid/util/DisplayMetrics;->scaledDensity:F

    div-float/2addr v1, v2

    iput v1, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->defSize:F

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->fullInvalidate()V

    :cond_25
    return-void
.end method

.method public setTextSize(IF)V
    .registers 6

    invoke-super {p0, p1, p2}, Lcom/android/systemui/statusbar/views/MiuiClock;->setTextSize(IF)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_25

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getClockSettings()Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getTextSize()F

    move-result v1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    invoke-virtual {v2}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v2

    iget v2, v2, Landroid/util/DisplayMetrics;->scaledDensity:F

    div-float/2addr v1, v2

    iput v1, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->defSize:F

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->fullInvalidate()V

    :cond_25
    return-void
.end method

.method public setTransitionAlpha(F)V
    .registers 3

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->setTransitionAlpha(F)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_a

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->setTransitionAlpha(F)V

    :cond_a
    return-void
.end method

.method public setTranslationX(F)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_7

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->setTranslationX(F)V

    :cond_7
    return-void
.end method

.method public setTranslationY(F)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_7

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->setTranslationY(F)V

    :cond_7
    return-void
.end method

.method public setVisibility(I)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_7

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->setVisibility(I)V

    :cond_7
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->setVisibility(I)V

    return-void
.end method

.method public updateLightDarkTint$2(Ljava/util/ArrayList;FIIIZ)V
    .registers 7

    invoke-super/range {p0 .. p6}, Lcom/android/systemui/statusbar/views/MiuiClock;->updateLightDarkTint$2(Ljava/util/ArrayList;FIIIZ)V

    return-void
.end method

.method public updateTime()V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockView;->clockLayout:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_3f

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getClockSettings()Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v0

    const-string v2, "clock_mezo_time_style"

    invoke-static {v2}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v2

    iget-boolean v0, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->isSecondEnable:Z

    if-eqz v0, :cond_1e

    if-eqz v2, :cond_1b

    const-string v1, "kk:mm:ss"

    goto :goto_25

    :cond_1b
    const-string v1, "h:mm:ss"

    goto :goto_25

    :cond_1e
    if-eqz v2, :cond_23

    const-string v1, "kk:mm"

    goto :goto_25

    :cond_23
    const-string v1, "h:mm"

    :goto_25
    invoke-static {}, Ljava/util/Calendar;->getInstance()Ljava/util/Calendar;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/text/format/DateFormat;->format(Ljava/lang/CharSequence;Ljava/util/Calendar;)Ljava/lang/CharSequence;

    move-result-object v1

    check-cast v1, Ljava/lang/String;

    const-string v2, ":"

    const-string v3, " "

    invoke-virtual {v1, v2, v3}, Ljava/lang/String;->replaceAll(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockView;->deleteZero(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockView;->setText(Ljava/lang/CharSequence;)V

    return-void

    :cond_3f
    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiClock;->updateTime()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_clock_ClockView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
