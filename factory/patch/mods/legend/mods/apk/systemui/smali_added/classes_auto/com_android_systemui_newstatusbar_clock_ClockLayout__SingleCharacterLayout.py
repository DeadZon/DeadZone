"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout.smali'
CLASS_FALLBACK_NAMES = ['ClockLayout$SingleCharacterLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;
.super Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/clock/ClockLayout;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x2
    name = "SingleCharacterLayout"
.end annotation


# instance fields
.field private isNeedChangeAnimStyle:Z

.field private text:Ljava/lang/String;

.field final synthetic this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;


# direct methods
.method public constructor <init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout;Landroid/content/Context;)V
    .registers 3

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    invoke-direct {p0, p2}, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;-><init>(Landroid/content/Context;)V

    const-string p1, ""

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->text:Ljava/lang/String;

    const/4 p1, 0x0

    iput-boolean p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->isNeedChangeAnimStyle:Z

    return-void
.end method

.method private deleteSpase(Ljava/lang/String;)Ljava/lang/String;
    .registers 4

    invoke-virtual {p1}, Ljava/lang/String;->isEmpty()Z

    move-result v0

    if-nez v0, :cond_14

    const-string v0, " "

    invoke-virtual {p1, v0}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result v0

    if-lez v0, :cond_14

    const/4 v0, 0x0

    const/4 v1, 0x1

    invoke-virtual {p1, v0, v1}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object p1

    :cond_14
    return-object p1
.end method


# virtual methods
.method protected createView(Landroid/widget/FrameLayout;I)Lcom/android/systemui/newstatusbar/clock/IClock;
    .registers 6

    goto/32 :goto_1f

    nop

    :goto_4
    const/4 v2, -0x2

    goto/32 :goto_39

    nop

    :goto_9
    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;-><init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout;Landroid/content/Context;)V

    goto/32 :goto_26

    nop

    :goto_10
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->getContext()Landroid/content/Context;

    move-result-object v2

    goto/32 :goto_9

    nop

    :goto_18
    invoke-virtual {p1, v0, p2}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;I)V

    goto/32 :goto_25

    nop

    :goto_1f
    new-instance v0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_2c

    nop

    :goto_25
    return-object v0

    :goto_26
    new-instance v1, Landroid/view/ViewGroup$LayoutParams;

    goto/32 :goto_4

    nop

    :goto_2c
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    goto/32 :goto_10

    nop

    :goto_32
    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    goto/32 :goto_18

    nop

    :goto_39
    invoke-direct {v1, v2, v2}, Landroid/view/ViewGroup$LayoutParams;-><init>(II)V

    goto/32 :goto_32

    nop
.end method

.method protected initialize()V
    .registers 3

    goto/32 :goto_2c

    nop

    :goto_4
    check-cast v1, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_36

    nop

    :goto_a
    invoke-virtual {p0, p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->createView(Landroid/widget/FrameLayout;I)Lcom/android/systemui/newstatusbar/clock/IClock;

    move-result-object v1

    goto/32 :goto_1e

    nop

    :goto_12
    iput-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    goto/32 :goto_31

    nop

    :goto_18
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    goto/32 :goto_4

    nop

    :goto_1e
    iput-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    goto/32 :goto_18

    nop

    :goto_24
    invoke-virtual {p0, p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->createView(Landroid/widget/FrameLayout;I)Lcom/android/systemui/newstatusbar/clock/IClock;

    move-result-object v1

    goto/32 :goto_12

    nop

    :goto_2c
    const/4 v0, 0x0

    goto/32 :goto_24

    nop

    :goto_31
    const/4 v1, 0x1

    goto/32 :goto_a

    nop

    :goto_36
    iput-boolean v0, v1, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->mActive:Z

    goto/32 :goto_3c

    nop

    :goto_3c
    return-void
.end method

.method protected onMeasure(II)V
    .registers 5

    goto/32 :goto_40

    nop

    :goto_4
    float-to-int v0, v0

    goto/32 :goto_17

    nop

    :goto_9
    invoke-virtual {v0}, Landroid/widget/TextView;->getPaint()Landroid/text/TextPaint;

    move-result-object v0

    goto/32 :goto_33

    nop

    :goto_11
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    goto/32 :goto_3a

    nop

    :goto_17
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->getTextHeight()F

    move-result v1

    goto/32 :goto_27

    nop

    :goto_1f
    invoke-virtual {v0, v1}, Landroid/text/TextPaint;->measureText(Ljava/lang/String;)F

    move-result v0

    goto/32 :goto_4

    nop

    :goto_27
    float-to-int v1, v1

    goto/32 :goto_2c

    nop

    :goto_2c
    invoke-virtual {p0, v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->setMeasuredDimension(II)V

    goto/32 :goto_39

    nop

    :goto_33
    const-string v1, "0"

    goto/32 :goto_1f

    nop

    :goto_39
    return-void

    :goto_3a
    check-cast v0, Landroid/widget/TextView;

    goto/32 :goto_9

    nop

    :goto_40
    invoke-super {p0, p1, p2}, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->onMeasure(II)V

    goto/32 :goto_11

    nop
.end method

.method public onTextChanged(Ljava/lang/CharSequence;)V
    .registers 5

    invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->deleteSpase(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->text:Ljava/lang/String;

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->deleteSpase(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_2d

    invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->text:Ljava/lang/String;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v1

    const/4 v2, 0x1

    invoke-interface {v0, v1, v2}, Lcom/android/systemui/newstatusbar/clock/IClock;->setText(Ljava/lang/String;Z)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-interface {v0, v1, v2}, Lcom/android/systemui/newstatusbar/clock/IClock;->setText(Ljava/lang/String;Z)V

    :cond_2d
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_clock_ClockLayout_SingleCharacterLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
