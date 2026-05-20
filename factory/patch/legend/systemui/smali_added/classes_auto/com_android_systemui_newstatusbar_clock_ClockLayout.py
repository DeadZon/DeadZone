"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/clock/ClockLayout.smali'
CLASS_FALLBACK_NAMES = ['ClockLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/clock/ClockLayout;
.super Lcom/android/systemui/newstatusbar/clock/ClockLayoutExt;

# interfaces
.implements Lcom/android/systemui/newstatusbar/clock/SecondTick$CallBack;
.implements Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;,
        Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;,
        Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;
    }
.end annotation


# static fields
.field public static final TAG:Ljava/lang/String; = "clock_app"


# instance fields
.field private animDots:Landroid/view/animation/AlphaAnimation;

.field private final clock:Lcom/android/systemui/newstatusbar/clock/ClockView;

.field public clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

.field private dataUpdatedToStatus:Z

.field protected final dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

.field private isExpand:Z

.field private final secondTick:Lcom/android/systemui/newstatusbar/clock/SecondTick;

.field protected thirdCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;


# direct methods
.method public constructor <init>(Landroid/content/Context;Lcom/android/systemui/newstatusbar/clock/ClockView;)V
    .registers 4

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutExt;-><init>(Landroid/content/Context;)V

    const/4 v0, 0x2

    new-array v0, v0, [Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    iput-object p2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clock:Lcom/android/systemui/newstatusbar/clock/ClockView;

    new-instance v0, Lcom/android/systemui/newstatusbar/clock/SecondTick;

    invoke-direct {v0, p1}, Lcom/android/systemui/newstatusbar/clock/SecondTick;-><init>(Landroid/content/Context;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->secondTick:Lcom/android/systemui/newstatusbar/clock/SecondTick;

    const/4 v0, 0x1

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->setWillNotDraw(Z)V

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/clock/ClockLayout;)Lcom/android/systemui/newstatusbar/clock/ClockView;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clock:Lcom/android/systemui/newstatusbar/clock/ClockView;

    return-object v0
.end method

.method private hasRunning()Z
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->animDots:Landroid/view/animation/AlphaAnimation;

    if-eqz v0, :cond_10

    invoke-virtual {v0}, Landroid/view/animation/AlphaAnimation;->hasStarted()Z

    move-result v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->animDots:Landroid/view/animation/AlphaAnimation;

    invoke-virtual {v1}, Landroid/view/animation/AlphaAnimation;->hasEnded()Z

    move-result v1

    xor-int/2addr v0, v1

    return v0

    :cond_10
    const/4 v0, 0x0

    return v0
.end method

.method private isOneDigitsFirst()Z
    .registers 5

    const/4 v0, 0x0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clock:Lcom/android/systemui/newstatusbar/clock/ClockView;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getText()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/String;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/String;->length()I

    move-result v2

    if-lez v2, :cond_18

    const/4 v2, 0x1

    const-string v3, " "

    invoke-virtual {v1, v3, v2}, Ljava/lang/String;->startsWith(Ljava/lang/String;I)Z

    move-result v0

    :cond_18
    return v0
.end method


# virtual methods
.method public asView()Lcom/android/systemui/newstatusbar/clock/ClockLayout;
    .registers 1

    return-object p0
.end method

.method protected createView(Landroid/widget/LinearLayout;I)Lcom/android/systemui/newstatusbar/clock/IClock;
    .registers 6

    goto/32 :goto_3a

    nop

    :goto_4
    invoke-direct {v1, v2, v2}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V

    goto/32 :goto_b

    nop

    :goto_b
    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    goto/32 :goto_2b

    nop

    :goto_12
    invoke-direct {v0, p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;-><init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout;Landroid/content/Context;)V

    goto/32 :goto_19

    nop

    :goto_19
    new-instance v1, Landroid/widget/LinearLayout$LayoutParams;

    goto/32 :goto_26

    nop

    :goto_1f
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;->initialize()V

    goto/32 :goto_40

    nop

    :goto_26
    const/4 v2, -0x2

    goto/32 :goto_4

    nop

    :goto_2b
    invoke-virtual {p1, v0, p2}, Landroid/widget/LinearLayout;->addView(Landroid/view/View;I)V

    goto/32 :goto_1f

    nop

    :goto_32
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getContext()Landroid/content/Context;

    move-result-object v1

    goto/32 :goto_12

    nop

    :goto_3a
    new-instance v0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;

    goto/32 :goto_32

    nop

    :goto_40
    return-object v0
.end method

.method public fullInvalidate()V
    .registers 5

    invoke-super {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutExt;->fullInvalidate()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->thirdCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0}, Lcom/android/systemui/newstatusbar/clock/IClock;->fullInvalidate()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    array-length v1, v0

    const/4 v2, 0x0

    :goto_c
    if-ge v2, v1, :cond_16

    aget-object v3, v0, v2

    invoke-interface {v3}, Lcom/android/systemui/newstatusbar/clock/IClock;->fullInvalidate()V

    add-int/lit8 v2, v2, 0x1

    goto :goto_c

    :cond_16
    return-void
.end method

.method public getClockSettings()Lcom/android/systemui/newstatusbar/clock/ClockSettings;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    return-object v0
.end method

.method protected initialize()V
    .registers 9

    goto/32 :goto_fd

    nop

    :goto_4
    iget-object v0, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->key:Ljava/lang/String;

    goto/32 :goto_114

    nop

    :goto_a
    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    goto/32 :goto_32

    nop

    :goto_12
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getContext()Landroid/content/Context;

    move-result-object v7

    goto/32 :goto_165

    nop

    :goto_1a
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clock:Lcom/android/systemui/newstatusbar/clock/ClockView;

    goto/32 :goto_77

    nop

    :goto_20
    const/4 v4, -0x1

    goto/32 :goto_b6

    nop

    :goto_25
    iput-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    goto/32 :goto_57

    nop

    :goto_2b
    invoke-direct {v2, p0, v3}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;-><init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout;Landroid/content/Context;)V

    goto/32 :goto_9e

    nop

    :goto_32
    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->isExpand:Z

    goto/32 :goto_103

    nop

    :goto_38
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->thirdCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    goto/32 :goto_158

    nop

    :goto_3e
    aget-object v1, v1, v2

    goto/32 :goto_133

    nop

    :goto_44
    aget-object v1, v1, v2

    goto/32 :goto_f2

    nop

    :goto_4a
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_7e

    nop

    :goto_50
    invoke-virtual {v1, v6}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    goto/32 :goto_63

    nop

    :goto_57
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_69

    nop

    :goto_5d
    aget-object v1, v1, v0

    goto/32 :goto_15f

    nop

    :goto_63
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_44

    nop

    :goto_69
    new-instance v6, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_12

    nop

    :goto_6f
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getContext()Landroid/content/Context;

    move-result-object v3

    goto/32 :goto_2b

    nop

    :goto_77
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->updateTime()V

    goto/32 :goto_b5

    nop

    :goto_7e
    new-instance v2, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_6f

    nop

    :goto_84
    iput-boolean v2, v1, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->isDot:Z

    goto/32 :goto_108

    nop

    :goto_8a
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_90

    nop

    :goto_90
    aget-object v1, v1, v2

    goto/32 :goto_12d

    nop

    :goto_96
    invoke-virtual {p0, p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->createView(Landroid/widget/LinearLayout;I)Lcom/android/systemui/newstatusbar/clock/IClock;

    move-result-object v0

    goto/32 :goto_38

    nop

    :goto_9e
    aput-object v2, v1, v0

    goto/32 :goto_bd

    nop

    :goto_a4
    new-instance v2, Landroid/widget/LinearLayout$LayoutParams;

    goto/32 :goto_cf

    nop

    :goto_aa
    const/4 v1, 0x2

    goto/32 :goto_d4

    nop

    :goto_af
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_f7

    nop

    :goto_b5
    return-void

    :goto_b6
    invoke-direct {v2, v3, v4}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V

    goto/32 :goto_140

    nop

    :goto_bd
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_13a

    nop

    :goto_c3
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_c9

    nop

    :goto_c9
    aget-object v1, v1, v2

    goto/32 :goto_84

    nop

    :goto_cf
    const/4 v3, -0x2

    goto/32 :goto_20

    nop

    :goto_d4
    invoke-virtual {p0, p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->createView(Landroid/widget/LinearLayout;I)Lcom/android/systemui/newstatusbar/clock/IClock;

    move-result-object v1

    goto/32 :goto_25

    nop

    :goto_dc
    invoke-virtual {p0, p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->createView(Landroid/widget/LinearLayout;I)Lcom/android/systemui/newstatusbar/clock/IClock;

    move-result-object v1

    goto/32 :goto_ec

    nop

    :goto_e4
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v0

    goto/32 :goto_4

    nop

    :goto_ec
    iput-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    goto/32 :goto_4a

    nop

    :goto_f2
    const/4 v3, 0x3

    goto/32 :goto_172

    nop

    :goto_f7
    aget-object v1, v1, v0

    goto/32 :goto_179

    nop

    :goto_fd
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    goto/32 :goto_e4

    nop

    :goto_103
    const/4 v0, 0x0

    goto/32 :goto_dc

    nop

    :goto_108
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_3e

    nop

    :goto_10e
    aget-object v1, v1, v0

    goto/32 :goto_153

    nop

    :goto_114
    const-string v1, "expanded_clock"

    goto/32 :goto_a

    nop

    :goto_11a
    aput-object v6, v1, v2

    goto/32 :goto_8a

    nop

    :goto_120
    invoke-virtual {p0, v1, v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->addView(Landroid/view/View;I)V

    goto/32 :goto_127

    nop

    :goto_127
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_5d

    nop

    :goto_12d
    new-instance v6, Landroid/widget/LinearLayout$LayoutParams;

    goto/32 :goto_14c

    nop

    :goto_133
    invoke-virtual {v1, v5, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setText(Ljava/lang/String;Z)V

    goto/32 :goto_147

    nop

    :goto_13a
    aget-object v1, v1, v0

    goto/32 :goto_a4

    nop

    :goto_140
    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    goto/32 :goto_16c

    nop

    :goto_147
    const/4 v0, 0x4

    goto/32 :goto_96

    nop

    :goto_14c
    invoke-direct {v6, v3, v4}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V

    goto/32 :goto_50

    nop

    :goto_153
    const/4 v2, 0x1

    goto/32 :goto_120

    nop

    :goto_158
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->updateSettings()V

    goto/32 :goto_186

    nop

    :goto_15f
    iput-boolean v2, v1, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->isDot:Z

    goto/32 :goto_af

    nop

    :goto_165
    invoke-direct {v6, p0, v7}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;-><init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout;Landroid/content/Context;)V

    goto/32 :goto_11a

    nop

    :goto_16c
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_10e

    nop

    :goto_172
    invoke-virtual {p0, v1, v3}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->addView(Landroid/view/View;I)V

    goto/32 :goto_c3

    nop

    :goto_179
    const-string v5, ":"

    goto/32 :goto_17f

    nop

    :goto_17f
    invoke-virtual {v1, v5, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setText(Ljava/lang/String;Z)V

    goto/32 :goto_aa

    nop

    :goto_186
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->updateSecondEnable()V

    goto/32 :goto_1a

    nop
.end method

.method public isSecondEnable()Z
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v0

    iget-boolean v0, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->isSecondEnable:Z

    return v0
.end method

.method public isStatus()Z
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v0

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->key:Ljava/lang/String;

    const-string v1, "status_clock"

    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    return v0
.end method

.method protected onAttachedToWindow()V
    .registers 2

    goto/32 :goto_19

    nop

    :goto_4
    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    goto/32 :goto_13

    nop

    :goto_c
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;)V

    goto/32 :goto_26

    nop

    :goto_13
    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    goto/32 :goto_c

    nop

    :goto_19
    invoke-super {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutExt;->onAttachedToWindow()V

    goto/32 :goto_20

    nop

    :goto_20
    const-class v0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    goto/32 :goto_4

    nop

    :goto_26
    return-void
.end method

.method protected onDetachedFromWindow()V
    .registers 2

    goto/32 :goto_20

    nop

    :goto_4
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;)V

    goto/32 :goto_11

    nop

    :goto_b
    const-class v0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    goto/32 :goto_18

    nop

    :goto_11
    return-void

    :goto_12
    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    goto/32 :goto_4

    nop

    :goto_18
    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    goto/32 :goto_12

    nop

    :goto_20
    invoke-super {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutExt;->onDetachedFromWindow()V

    goto/32 :goto_b

    nop
.end method

.method protected onLayout(ZIIII)V
    .registers 10

    goto/32 :goto_14

    nop

    :goto_4
    invoke-virtual {v0, v3, v3, v1, v2}, Lcom/android/systemui/newstatusbar/clock/ClockView;->layout(IIII)V

    :goto_7
    goto/32 :goto_1b

    nop

    :goto_b
    if-nez v0, :cond_10

    goto/32 :goto_7

    :cond_10
    goto/32 :goto_29

    nop

    :goto_14
    invoke-super/range {p0 .. p5}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutExt;->onLayout(ZIIII)V

    goto/32 :goto_31

    nop

    :goto_1b
    return-void

    :goto_1c
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getHeight()I

    move-result v2

    goto/32 :goto_24

    nop

    :goto_24
    const/4 v3, 0x0

    goto/32 :goto_4

    nop

    :goto_29
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getWidth()I

    move-result v1

    goto/32 :goto_1c

    nop

    :goto_31
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clock:Lcom/android/systemui/newstatusbar/clock/ClockView;

    goto/32 :goto_b

    nop
.end method

.method protected onMeasure(II)V
    .registers 9

    goto/32 :goto_12

    nop

    :goto_4
    invoke-virtual {v0, v2}, Landroid/graphics/Paint;->measureText(Ljava/lang/String;)F

    move-result v3

    goto/32 :goto_9d

    nop

    :goto_c
    goto/16 :goto_90

    :goto_e
    goto/32 :goto_75

    nop

    :goto_12
    invoke-super {p0, p1, p2}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutExt;->onMeasure(II)V

    goto/32 :goto_cf

    nop

    :goto_19
    if-nez v2, :cond_1e

    goto/32 :goto_71

    :cond_1e
    goto/32 :goto_4a

    nop

    :goto_22
    float-to-int v5, v5

    goto/32 :goto_50

    nop

    :goto_27
    const-string v4, "0"

    goto/32 :goto_d5

    nop

    :goto_2d
    const-string v2, "0:00:00"

    goto/32 :goto_33

    nop

    :goto_33
    goto :goto_90

    :goto_34
    goto/32 :goto_88

    nop

    :goto_38
    iget-object v5, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    goto/32 :goto_5f

    nop

    :goto_3e
    const/high16 v5, 0x40000000  # 2.0f

    goto/32 :goto_c9

    nop

    :goto_44
    iget-boolean v2, v1, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->isSecondEnable:Z

    goto/32 :goto_eb

    nop

    :goto_4a
    const-string v2, "0:00"

    goto/32 :goto_70

    nop

    :goto_50
    invoke-virtual {p0, v4, v5}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->setMeasuredDimension(II)V

    :goto_53
    goto/32 :goto_ce

    nop

    :goto_57
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->isOneDigitsFirst()Z

    move-result v2

    goto/32 :goto_b6

    nop

    :goto_5f
    invoke-interface {v5}, Lcom/android/systemui/newstatusbar/clock/IClock;->getTextHeight()F

    move-result v5

    goto/32 :goto_22

    nop

    :goto_67
    if-nez v0, :cond_6c

    goto/32 :goto_53

    :cond_6c
    goto/32 :goto_82

    nop

    :goto_70
    goto :goto_90

    :goto_71
    goto/32 :goto_8e

    nop

    :goto_75
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->isOneDigitsFirst()Z

    move-result v2

    goto/32 :goto_19

    nop

    :goto_7d
    const/4 v1, 0x0

    goto/32 :goto_e5

    nop

    :goto_82
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_7d

    nop

    :goto_88
    const-string v2, "00:00:00"

    goto/32 :goto_c

    nop

    :goto_8e
    const-string v2, "00:00"

    :goto_90
    goto/32 :goto_4

    nop

    :goto_94
    if-gt v4, v5, :cond_99

    goto/32 :goto_c5

    :cond_99
    goto/32 :goto_27

    nop

    :goto_9d
    iget v4, v1, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->typeFaseStyle:I

    goto/32 :goto_b1

    nop

    :goto_a3
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    goto/32 :goto_a9

    nop

    :goto_a9
    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v1

    goto/32 :goto_44

    nop

    :goto_b1
    const/4 v5, 0x1

    goto/32 :goto_94

    nop

    :goto_b6
    if-nez v2, :cond_bb

    goto/32 :goto_34

    :cond_bb
    goto/32 :goto_2d

    nop

    :goto_bf
    float-to-int v4, v3

    goto/32 :goto_38

    nop

    :goto_c4
    add-float/2addr v3, v4

    :goto_c5
    goto/32 :goto_bf

    nop

    :goto_c9
    div-float/2addr v4, v5

    goto/32 :goto_c4

    nop

    :goto_ce
    return-void

    :goto_cf
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    goto/32 :goto_67

    nop

    :goto_d5
    invoke-virtual {v0, v4}, Landroid/graphics/Paint;->measureText(Ljava/lang/String;)F

    move-result v4

    goto/32 :goto_3e

    nop

    :goto_dd
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->getPaint()Landroid/text/TextPaint;

    move-result-object v0

    goto/32 :goto_a3

    nop

    :goto_e5
    aget-object v0, v0, v1

    goto/32 :goto_dd

    nop

    :goto_eb
    if-nez v2, :cond_f0

    goto/32 :goto_e

    :cond_f0
    goto/32 :goto_57

    nop
.end method

.method public onTextChanged(Ljava/lang/CharSequence;)V
    .registers 9

    invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v1, " "

    invoke-virtual {v0, v1}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result v0

    if-lez v0, :cond_55

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v2

    invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v3

    const/4 v4, 0x0

    invoke-virtual {v3, v4, v0}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object v3

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v4, v3}, Lcom/android/systemui/newstatusbar/clock/IClock;->onTextChanged(Ljava/lang/CharSequence;)V

    invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v4

    add-int/lit8 v5, v0, 0x1

    add-int/lit8 v6, v0, 0x3

    invoke-virtual {v4, v5, v6}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object v3

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v4, v3}, Lcom/android/systemui/newstatusbar/clock/IClock;->onTextChanged(Ljava/lang/CharSequence;)V

    iget-boolean v4, v2, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->isSecondEnable:Z

    if-eqz v4, :cond_50

    invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v4, v1}, Ljava/lang/String;->lastIndexOf(Ljava/lang/String;)I

    move-result v0

    invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v1

    add-int/lit8 v4, v0, 0x1

    invoke-interface {p1}, Ljava/lang/CharSequence;->length()I

    move-result v5

    invoke-virtual {v1, v4, v5}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object v3

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->thirdCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v1, v3}, Lcom/android/systemui/newstatusbar/clock/IClock;->onTextChanged(Ljava/lang/CharSequence;)V

    :cond_50
    iget-boolean v1, v2, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->isDotsEnable:Z

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->startAnimDots(Z)V

    :cond_55
    return-void
.end method

.method public onVisibilityAggregated(Z)V
    .registers 4

    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutExt;->onVisibilityAggregated(Z)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clock:Lcom/android/systemui/newstatusbar/clock/ClockView;

    if-eqz v0, :cond_3e

    if-eqz p1, :cond_c

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->updateTime()V

    :cond_c
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->isExpand:Z

    if-nez v0, :cond_3e

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "onVisibilityAggregated: al = "

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clock:Lcom/android/systemui/newstatusbar/clock/ClockView;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getAlpha()F

    move-result v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(F)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "  trAl = "

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clock:Lcom/android/systemui/newstatusbar/clock/ClockView;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getTransitionAlpha()F

    move-result v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(F)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v1, "clock_app"

    invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_3e
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    if-eqz v0, :cond_6f

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->isExpand:Z

    if-eqz v0, :cond_53

    if-eqz p1, :cond_53

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->updateLoc()V

    :cond_53
    const/4 v0, 0x0

    if-eqz p1, :cond_62

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v1

    iget-boolean v1, v1, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->isDotsEnable:Z

    if-eqz v1, :cond_62

    const/4 v1, 0x1

    goto :goto_63

    :cond_62
    move v1, v0

    :goto_63
    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->startAnimDots(Z)V

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->isExpand:Z

    if-eqz v1, :cond_6f

    if-nez p1, :cond_6f

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->refreshClockSettings(Z)V

    :cond_6f
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->secondTick:Lcom/android/systemui/newstatusbar/clock/SecondTick;

    if-eqz v0, :cond_76

    invoke-virtual {v0, p0, p1}, Lcom/android/systemui/newstatusbar/clock/SecondTick;->onVisibleChange(Lcom/android/systemui/newstatusbar/clock/SecondTick$CallBack;Z)V

    :cond_76
    return-void
.end method

.method protected onVisibilityChanged(Landroid/view/View;I)V
    .registers 4

    goto/32 :goto_1b

    nop

    :goto_4
    if-eq p1, p0, :cond_9

    goto/32 :goto_16

    :cond_9
    goto/32 :goto_22

    nop

    :goto_d
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clock:Lcom/android/systemui/newstatusbar/clock/ClockView;

    goto/32 :goto_13

    nop

    :goto_13
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->updateTime()V

    :goto_16
    goto/32 :goto_1a

    nop

    :goto_1a
    return-void

    :goto_1b
    invoke-super {p0, p1, p2}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutExt;->onVisibilityChanged(Landroid/view/View;I)V

    goto/32 :goto_4

    nop

    :goto_22
    if-eqz p2, :cond_27

    goto/32 :goto_16

    :cond_27
    goto/32 :goto_d

    nop
.end method

.method public refreshClockSettings(Z)V
    .registers 6

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v0

    const/4 v1, 0x0

    if-eqz p1, :cond_15

    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dataUpdatedToStatus:Z

    if-nez v2, :cond_15

    const/4 v2, 0x1

    iput-boolean v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dataUpdatedToStatus:Z

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->updateToStatus()V

    const/4 v1, 0x1

    goto :goto_22

    :cond_15
    if-nez p1, :cond_22

    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dataUpdatedToStatus:Z

    if-eqz v2, :cond_22

    const/4 v2, 0x0

    iput-boolean v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dataUpdatedToStatus:Z

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->update()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    const/4 v1, 0x1

    :cond_22
    :goto_22
    if-nez v1, :cond_25

    return-void

    :cond_25
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->updateSecondEnable()V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clock:Lcom/android/systemui/newstatusbar/clock/ClockView;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->getSize()F

    move-result v3

    invoke-virtual {v2, v3}, Lcom/android/systemui/newstatusbar/clock/ClockView;->setTextSize(F)V

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->getSize()F

    move-result v2

    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->setTextSize(F)V

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->getTypeFace()Landroid/graphics/Typeface;

    move-result-object v2

    iget v3, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->typeFaseStyle:I

    invoke-virtual {p0, v2, v3}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->updateTypeface(Landroid/graphics/Typeface;I)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->fullInvalidate()V

    iget-boolean v2, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->isSecondEnable:Z

    if-nez v2, :cond_4d

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clock:Lcom/android/systemui/newstatusbar/clock/ClockView;

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/clock/ClockView;->updateTime()V

    :cond_4d
    iget-boolean v2, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->isSecondEnable:Z

    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->startAnimDots(Z)V

    return-void
.end method

.method public secondTick()V
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clock:Lcom/android/systemui/newstatusbar/clock/ClockView;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->updateTime()V

    return-void
.end method

.method public setTextSize(F)V
    .registers 6

    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutExt;->setTextSize(F)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    array-length v1, v0

    const/4 v2, 0x0

    :goto_7
    if-ge v2, v1, :cond_11

    aget-object v3, v0, v2

    invoke-interface {v3, p1}, Lcom/android/systemui/newstatusbar/clock/IClock;->setTextSize(F)V

    add-int/lit8 v2, v2, 0x1

    goto :goto_7

    :cond_11
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->thirdCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0, p1}, Lcom/android/systemui/newstatusbar/clock/IClock;->setTextSize(F)V

    return-void
.end method

.method public setTextSizeWidthAnimation(F)V
    .registers 6

    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutExt;->setTextSizeWidthAnimation(F)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    array-length v1, v0

    const/4 v2, 0x0

    :goto_7
    if-ge v2, v1, :cond_11

    aget-object v3, v0, v2

    invoke-interface {v3, p1}, Lcom/android/systemui/newstatusbar/clock/IClock;->setTextSizeWidthAnimation(F)V

    add-int/lit8 v2, v2, 0x1

    goto :goto_7

    :cond_11
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->thirdCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0, p1}, Lcom/android/systemui/newstatusbar/clock/IClock;->setTextSizeWidthAnimation(F)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clock:Lcom/android/systemui/newstatusbar/clock/ClockView;

    if-eqz v0, :cond_1d

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->updateTime()V

    :cond_1d
    return-void
.end method

.method public setVisibility(I)V
    .registers 3

    const/16 v0, 0x8

    if-ne p1, v0, :cond_5

    const/4 p1, 0x4

    :cond_5
    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutExt;->setVisibility(I)V

    return-void
.end method

.method protected startAnimDots(Z)V
    .registers 5

    goto/32 :goto_c8

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    goto/32 :goto_58

    nop

    :goto_a
    const/4 v1, 0x0

    goto/32 :goto_4c

    nop

    :goto_f
    invoke-virtual {v0, v1, v2}, Landroid/view/animation/AlphaAnimation;->setDuration(J)V

    goto/32 :goto_2e

    nop

    :goto_16
    const/4 v1, 0x1

    goto/32 :goto_e9

    nop

    :goto_1b
    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setAnimation(Landroid/view/animation/Animation;)V

    goto/32 :goto_4

    nop

    :goto_22
    iget-boolean v0, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->isSecondEnable:Z

    goto/32 :goto_39

    nop

    :goto_28
    new-instance v1, Lcom/android/systemui/newstatusbar/clock/ClockLayout$1;

    goto/32 :goto_e2

    nop

    :goto_2e
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->animDots:Landroid/view/animation/AlphaAnimation;

    goto/32 :goto_79

    nop

    :goto_34
    const/4 v1, 0x2

    goto/32 :goto_d5

    nop

    :goto_39
    if-nez v0, :cond_3e

    goto/32 :goto_a0

    :cond_3e
    goto/32 :goto_52

    nop

    :goto_42
    if-eqz p1, :cond_47

    goto/32 :goto_80

    :cond_47
    goto/32 :goto_66

    nop

    :goto_4b
    return-void

    :goto_4c
    aget-object v0, v0, v1

    goto/32 :goto_73

    nop

    :goto_52
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_16

    nop

    :goto_58
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v0

    goto/32 :goto_22

    nop

    :goto_60
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    goto/32 :goto_a

    nop

    :goto_66
    invoke-virtual {v0}, Landroid/view/animation/AlphaAnimation;->cancel()V

    goto/32 :goto_7f

    nop

    :goto_6d
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->animDots:Landroid/view/animation/AlphaAnimation;

    goto/32 :goto_84

    nop

    :goto_73
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->animDots:Landroid/view/animation/AlphaAnimation;

    goto/32 :goto_1b

    nop

    :goto_79
    const/16 v1, 0x46

    goto/32 :goto_ac

    nop

    :goto_7f
    return-void

    :goto_80
    goto/32 :goto_10a

    nop

    :goto_84
    invoke-virtual {v0}, Landroid/view/animation/AlphaAnimation;->start()V

    :goto_87
    goto/32 :goto_4b

    nop

    :goto_8b
    invoke-direct {v0, v1, v2}, Landroid/view/animation/AlphaAnimation;-><init>(FF)V

    goto/32 :goto_f8

    nop

    :goto_92
    const/4 v2, 0x0

    goto/32 :goto_8b

    nop

    :goto_97
    const-wide/16 v1, 0x3de

    goto/32 :goto_f

    nop

    :goto_9d
    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setAnimation(Landroid/view/animation/Animation;)V

    :goto_a0
    goto/32 :goto_6d

    nop

    :goto_a4
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->hasRunning()Z

    move-result v0

    goto/32 :goto_ef

    nop

    :goto_ac
    invoke-virtual {v0, v1}, Landroid/view/animation/AlphaAnimation;->setRepeatCount(I)V

    goto/32 :goto_b3

    nop

    :goto_b3
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->animDots:Landroid/view/animation/AlphaAnimation;

    goto/32 :goto_34

    nop

    :goto_b9
    if-nez v0, :cond_be

    goto/32 :goto_80

    :cond_be
    goto/32 :goto_42

    nop

    :goto_c2
    const/high16 v1, 0x3f800000  # 1.0f

    goto/32 :goto_92

    nop

    :goto_c8
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->animDots:Landroid/view/animation/AlphaAnimation;

    goto/32 :goto_b9

    nop

    :goto_ce
    invoke-virtual {v0, v1}, Landroid/view/animation/AlphaAnimation;->setAnimationListener(Landroid/view/animation/Animation$AnimationListener;)V

    goto/32 :goto_60

    nop

    :goto_d5
    invoke-virtual {v0, v1}, Landroid/view/animation/AlphaAnimation;->setRepeatMode(I)V

    goto/32 :goto_104

    nop

    :goto_dc
    new-instance v0, Landroid/view/animation/AlphaAnimation;

    goto/32 :goto_c2

    nop

    :goto_e2
    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$1;-><init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout;)V

    goto/32 :goto_ce

    nop

    :goto_e9
    aget-object v0, v0, v1

    goto/32 :goto_fe

    nop

    :goto_ef
    if-eqz v0, :cond_f4

    goto/32 :goto_87

    :cond_f4
    goto/32 :goto_dc

    nop

    :goto_f8
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->animDots:Landroid/view/animation/AlphaAnimation;

    goto/32 :goto_97

    nop

    :goto_fe
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->animDots:Landroid/view/animation/AlphaAnimation;

    goto/32 :goto_9d

    nop

    :goto_104
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->animDots:Landroid/view/animation/AlphaAnimation;

    goto/32 :goto_28

    nop

    :goto_10a
    if-nez p1, :cond_10f

    goto/32 :goto_87

    :cond_10f
    goto/32 :goto_a4

    nop
.end method

.method public updateSecondEnable()V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v0

    iget-boolean v0, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->isSecondEnable:Z

    const/4 v1, 0x0

    if-eqz v0, :cond_d

    move v2, v1

    goto :goto_f

    :cond_d
    const/16 v2, 0x8

    :goto_f
    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->startAnimDots(Z)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v1

    iget-boolean v1, v1, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->isDotsEnable:Z

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->startAnimDots(Z)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->thirdCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v1, v2}, Lcom/android/systemui/newstatusbar/clock/IClock;->setVisibility(I)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    const/4 v3, 0x1

    aget-object v1, v1, v3

    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setVisibility(I)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->secondTick:Lcom/android/systemui/newstatusbar/clock/SecondTick;

    if-eqz v1, :cond_35

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->isShown()Z

    move-result v3

    invoke-virtual {v1, p0, v3}, Lcom/android/systemui/newstatusbar/clock/SecondTick;->onVisibleChange(Lcom/android/systemui/newstatusbar/clock/SecondTick$CallBack;Z)V

    :cond_35
    return-void
.end method

.method public updateSettings()V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->updateSecondEnable()V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clock:Lcom/android/systemui/newstatusbar/clock/ClockView;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->getSize()F

    move-result v2

    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/clock/ClockView;->setTextSize(F)V

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->getSize()F

    move-result v1

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->setTextSize(F)V

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->getTypeFace()Landroid/graphics/Typeface;

    move-result-object v1

    iget v2, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->typeFaseStyle:I

    invoke-virtual {p0, v1, v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->updateTypeface(Landroid/graphics/Typeface;I)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->fullInvalidate()V

    iget-boolean v1, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->isSecondEnable:Z

    if-nez v1, :cond_2e

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clock:Lcom/android/systemui/newstatusbar/clock/ClockView;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/clock/ClockView;->updateTime()V

    :cond_2e
    iget-boolean v1, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->isSecondEnable:Z

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->startAnimDots(Z)V

    const-class v1, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    invoke-static {v1}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    invoke-virtual {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;)V

    const-class v1, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    invoke-static {v1}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    invoke-virtual {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;)V

    return-void
.end method

.method public updateTypeface(Landroid/graphics/Typeface;I)V
    .registers 7

    invoke-super {p0, p1, p2}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutExt;->updateTypeface(Landroid/graphics/Typeface;I)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->thirdCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0, p1, p2}, Lcom/android/systemui/newstatusbar/clock/IClock;->updateTypeface(Landroid/graphics/Typeface;I)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->dots:[Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    array-length v1, v0

    const/4 v2, 0x0

    :goto_c
    if-ge v2, v1, :cond_16

    aget-object v3, v0, v2

    invoke-interface {v3, p1, p2}, Lcom/android/systemui/newstatusbar/clock/IClock;->updateTypeface(Landroid/graphics/Typeface;I)V

    add-int/lit8 v2, v2, 0x1

    goto :goto_c

    :cond_16
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_clock_ClockLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
