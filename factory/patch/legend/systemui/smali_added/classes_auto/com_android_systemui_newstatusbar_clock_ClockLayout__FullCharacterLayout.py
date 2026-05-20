"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout.smali'
CLASS_FALLBACK_NAMES = ['ClockLayout$FullCharacterLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;
.super Lcom/android/systemui/newstatusbar/clock/ClockLayoutExt;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/clock/ClockLayout;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x2
    name = "FullCharacterLayout"
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;


# direct methods
.method public constructor <init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout;Landroid/content/Context;)V
    .registers 3

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;->this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    invoke-direct {p0, p2}, Lcom/android/systemui/newstatusbar/clock/ClockLayoutExt;-><init>(Landroid/content/Context;)V

    return-void
.end method


# virtual methods
.method protected createView(Landroid/widget/LinearLayout;I)Lcom/android/systemui/newstatusbar/clock/IClock;
    .registers 6

    goto/32 :goto_3a

    nop

    :goto_4
    new-instance v1, Landroid/view/ViewGroup$LayoutParams;

    goto/32 :goto_b

    nop

    :goto_a
    return-object v0

    :goto_b
    const/4 v2, -0x2

    goto/32 :goto_17

    nop

    :goto_10
    invoke-virtual {p1, v0, p2, v1}, Landroid/widget/LinearLayout;->addView(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V

    goto/32 :goto_33

    nop

    :goto_17
    invoke-direct {v1, v2, v2}, Landroid/view/ViewGroup$LayoutParams;-><init>(II)V

    goto/32 :goto_10

    nop

    :goto_1e
    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;-><init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout;Landroid/content/Context;)V

    goto/32 :goto_4

    nop

    :goto_25
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;->getContext()Landroid/content/Context;

    move-result-object v2

    goto/32 :goto_1e

    nop

    :goto_2d
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;->this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    goto/32 :goto_25

    nop

    :goto_33
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;->initialize()V

    goto/32 :goto_a

    nop

    :goto_3a
    new-instance v0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$SingleCharacterLayout;

    goto/32 :goto_2d

    nop
.end method

.method protected initialize()V
    .registers 2

    goto/32 :goto_17

    nop

    :goto_4
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    goto/32 :goto_12

    nop

    :goto_a
    invoke-virtual {p0, p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;->createView(Landroid/widget/LinearLayout;I)Lcom/android/systemui/newstatusbar/clock/IClock;

    move-result-object v0

    goto/32 :goto_24

    nop

    :goto_12
    const/4 v0, 0x1

    goto/32 :goto_a

    nop

    :goto_17
    const/4 v0, 0x0

    goto/32 :goto_1c

    nop

    :goto_1c
    invoke-virtual {p0, p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;->createView(Landroid/widget/LinearLayout;I)Lcom/android/systemui/newstatusbar/clock/IClock;

    move-result-object v0

    goto/32 :goto_4

    nop

    :goto_24
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    goto/32 :goto_2a

    nop

    :goto_2a
    return-void
.end method

.method public onTextChanged(Ljava/lang/CharSequence;)V
    .registers 7

    invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/String;->isEmpty()Z

    move-result v0

    if-eqz v0, :cond_b

    return-void

    :cond_b
    invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v0

    const/4 v1, 0x0

    const/4 v2, 0x1

    invoke-virtual {v0, v1, v2}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v0}, Ljava/lang/String;->length()I

    move-result v4

    if-le v4, v2, :cond_33

    const-string v4, " "

    invoke-virtual {v0, v4}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result v4

    if-eq v4, v2, :cond_33

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v4, v1}, Lcom/android/systemui/newstatusbar/clock/IClock;->setVisibility(I)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v1, v3}, Lcom/android/systemui/newstatusbar/clock/IClock;->onTextChanged(Ljava/lang/CharSequence;)V

    const/4 v1, 0x2

    invoke-virtual {v0, v2, v1}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object v3

    goto :goto_3a

    :cond_33
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    const/16 v2, 0x8

    invoke-interface {v1, v2}, Lcom/android/systemui/newstatusbar/clock/IClock;->setVisibility(I)V

    :goto_3a
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$FullCharacterLayout;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v1, v3}, Lcom/android/systemui/newstatusbar/clock/IClock;->onTextChanged(Ljava/lang/CharSequence;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_clock_ClockLayout_FullCharacterLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
