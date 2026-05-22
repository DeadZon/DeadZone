"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock.smali'
CLASS_FALLBACK_NAMES = ['ClockLayoutWithMultiCock.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;
.super Lcom/android/systemui/newstatusbar/clock/ClockLayout;


# instance fields
.field private isFirstStart:Z

.field private isMultiClock:Z

.field private multiClockLayout:Landroid/view/View;

.field private final stokView:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/clock/IClock;",
            ">;"
        }
    .end annotation
.end field


# direct methods
.method public constructor <init>(Landroid/content/Context;Lcom/android/systemui/newstatusbar/clock/ClockView;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;-><init>(Landroid/content/Context;Lcom/android/systemui/newstatusbar/clock/ClockView;)V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->stokView:Ljava/util/ArrayList;

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->isFirstStart:Z

    return-void
.end method

.method private updateVisibility()V
    .registers 5

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->isFirstStart:Z

    const/4 v1, 0x0

    if-nez v0, :cond_41

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->isMultiClock:Z

    const/16 v2, 0x8

    if-eqz v0, :cond_2a

    invoke-super {p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->startAnimDots(Z)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->stokView:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_14
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    if-eqz v3, :cond_24

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v3, v2}, Lcom/android/systemui/newstatusbar/clock/IClock;->setVisibility(I)V

    goto :goto_14

    :cond_24
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->multiClockLayout:Landroid/view/View;

    invoke-virtual {v0, v1}, Landroid/view/View;->setVisibility(I)V

    goto :goto_40

    :cond_2a
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->multiClockLayout:Landroid/view/View;

    invoke-virtual {v0, v2}, Landroid/view/View;->setVisibility(I)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0, v1}, Lcom/android/systemui/newstatusbar/clock/IClock;->setVisibility(I)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0, v1}, Lcom/android/systemui/newstatusbar/clock/IClock;->setVisibility(I)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    aget-object v0, v0, v1

    invoke-interface {v0, v1}, Lcom/android/systemui/newstatusbar/clock/IClock;->setVisibility(I)V

    :goto_40
    return-void

    :cond_41
    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->isFirstStart:Z

    return-void
.end method


# virtual methods
.method protected initialize()V
    .registers 4

    goto/32 :goto_74

    nop

    :goto_4
    const/4 v2, 0x0

    goto/32 :goto_b6

    nop

    :goto_9
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->getContext()Landroid/content/Context;

    move-result-object v1

    goto/32 :goto_a2

    nop

    :goto_11
    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto/32 :goto_66

    nop

    :goto_18
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    goto/32 :goto_36

    nop

    :goto_1e
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_4

    nop

    :goto_24
    aget-object v1, v1, v2

    goto/32 :goto_9b

    nop

    :goto_2a
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->stokView:Ljava/util/ArrayList;

    goto/32 :goto_8e

    nop

    :goto_30
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_61

    nop

    :goto_36
    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto/32 :goto_55

    nop

    :goto_3d
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->stokView:Ljava/util/ArrayList;

    goto/32 :goto_18

    nop

    :goto_43
    const/4 v2, -0x2

    goto/32 :goto_6c

    nop

    :goto_48
    invoke-virtual {p0, v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    goto/32 :goto_7b

    nop

    :goto_4f
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->thirdCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    goto/32 :goto_a9

    nop

    :goto_55
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->stokView:Ljava/util/ArrayList;

    goto/32 :goto_4f

    nop

    :goto_5b
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->stokView:Ljava/util/ArrayList;

    goto/32 :goto_1e

    nop

    :goto_61
    const/4 v2, 0x1

    goto/32 :goto_24

    nop

    :goto_66
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->stokView:Ljava/util/ArrayList;

    goto/32 :goto_30

    nop

    :goto_6c
    invoke-direct {v1, v2, v2}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V

    goto/32 :goto_48

    nop

    :goto_73
    return-void

    :goto_74
    invoke-super {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->initialize()V

    goto/32 :goto_2a

    nop

    :goto_7b
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->updateSettings()V

    goto/32 :goto_73

    nop

    :goto_82
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->multiClockLayout:Landroid/view/View;

    goto/32 :goto_88

    nop

    :goto_88
    new-instance v1, Landroid/widget/LinearLayout$LayoutParams;

    goto/32 :goto_43

    nop

    :goto_8e
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    goto/32 :goto_94

    nop

    :goto_94
    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto/32 :goto_3d

    nop

    :goto_9b
    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto/32 :goto_b0

    nop

    :goto_a2
    invoke-direct {v0, v1}, Lcom/android/systemui/newstatusbar/clock/MultiClockView;-><init>(Landroid/content/Context;)V

    goto/32 :goto_82

    nop

    :goto_a9
    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto/32 :goto_5b

    nop

    :goto_b0
    new-instance v0, Lcom/android/systemui/newstatusbar/clock/MultiClockView;

    goto/32 :goto_9

    nop

    :goto_b6
    aget-object v1, v1, v2

    goto/32 :goto_11

    nop
.end method

.method protected onLayout(ZIIII)V
    .registers 10

    goto/32 :goto_14

    nop

    :goto_4
    if-nez v0, :cond_9

    goto/32 :goto_10

    :cond_9
    goto/32 :goto_24

    nop

    :goto_d
    invoke-virtual {v0, v3, v3, v1, v2}, Landroid/view/View;->layout(IIII)V

    :goto_10
    goto/32 :goto_23

    nop

    :goto_14
    invoke-super/range {p0 .. p5}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->onLayout(ZIIII)V

    goto/32 :goto_38

    nop

    :goto_1b
    invoke-virtual {v0}, Landroid/view/View;->getMeasuredWidth()I

    move-result v1

    goto/32 :goto_32

    nop

    :goto_23
    return-void

    :goto_24
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->multiClockLayout:Landroid/view/View;

    goto/32 :goto_1b

    nop

    :goto_2a
    invoke-virtual {v2}, Landroid/view/View;->getMeasuredHeight()I

    move-result v2

    goto/32 :goto_3e

    nop

    :goto_32
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->multiClockLayout:Landroid/view/View;

    goto/32 :goto_2a

    nop

    :goto_38
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->isMultiClock:Z

    goto/32 :goto_4

    nop

    :goto_3e
    const/4 v3, 0x0

    goto/32 :goto_d

    nop
.end method

.method protected onMeasure(II)V
    .registers 6

    goto/32 :goto_28

    nop

    :goto_4
    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->isMultiClock:Z

    goto/32 :goto_a

    nop

    :goto_a
    if-nez v1, :cond_f

    goto/32 :goto_5a

    :cond_f
    goto/32 :goto_2e

    nop

    :goto_13
    invoke-super {p0, p1, p2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->onMeasure(II)V

    goto/32 :goto_33

    nop

    :goto_1a
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->multiClockLayout:Landroid/view/View;

    goto/32 :goto_47

    nop

    :goto_20
    invoke-virtual {p0, v1, v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->setMeasuredDimension(II)V

    :goto_23
    goto/32 :goto_27

    nop

    :goto_27
    return-void

    :goto_28
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    goto/32 :goto_4

    nop

    :goto_2e
    const/4 v1, 0x0

    goto/32 :goto_58

    nop

    :goto_33
    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->isMultiClock:Z

    goto/32 :goto_64

    nop

    :goto_39
    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v1

    goto/32 :goto_41

    nop

    :goto_41
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->multiClockLayout:Landroid/view/View;

    goto/32 :goto_50

    nop

    :goto_47
    if-nez v1, :cond_4c

    goto/32 :goto_23

    :cond_4c
    goto/32 :goto_39

    nop

    :goto_50
    invoke-virtual {v2}, Landroid/view/View;->getMeasuredHeight()I

    move-result v2

    goto/32 :goto_20

    nop

    :goto_58
    iput-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    :goto_5a
    goto/32 :goto_13

    nop

    :goto_5e
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    goto/32 :goto_1a

    nop

    :goto_64
    if-nez v1, :cond_69

    goto/32 :goto_23

    :cond_69
    goto/32 :goto_5e

    nop
.end method

.method public onTextChanged(Ljava/lang/CharSequence;)V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->isMultiClock:Z

    if-nez v0, :cond_7

    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->onTextChanged(Ljava/lang/CharSequence;)V

    :cond_7
    return-void
.end method

.method public refreshClockSettings(Z)V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->isMultiClock:Z

    if-nez v0, :cond_7

    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->refreshClockSettings(Z)V

    :cond_7
    return-void
.end method

.method protected startAnimDots(Z)V
    .registers 3

    goto/32 :goto_4

    nop

    :goto_4
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->isMultiClock:Z

    goto/32 :goto_a

    nop

    :goto_a
    if-eqz v0, :cond_f

    goto/32 :goto_17

    :cond_f
    goto/32 :goto_14

    nop

    :goto_13
    return-void

    :goto_14
    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->startAnimDots(Z)V

    :goto_17
    goto/32 :goto_13

    nop
.end method

.method public updateSettings()V
    .registers 3

    const-string v0, "statusbar_clock_style"

    const/4 v1, -0x5

    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    if-lez v0, :cond_b

    const/4 v0, 0x1

    goto :goto_c

    :cond_b
    const/4 v0, 0x0

    :goto_c
    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->isMultiClock:Z

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->updateVisibility()V

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayoutWithMultiCock;->isMultiClock:Z

    if-nez v0, :cond_18

    invoke-super {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->updateSettings()V

    :cond_18
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_clock_ClockLayoutWithMultiCock',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
