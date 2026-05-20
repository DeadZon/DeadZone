"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/clock/ClockLayout$1.smali'
CLASS_FALLBACK_NAMES = ['ClockLayout$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/clock/ClockLayout$1;
.super Ljava/lang/Object;

# interfaces
.implements Landroid/view/animation/Animation$AnimationListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/newstatusbar/clock/ClockLayout;->startAnimDots(Z)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$1;->this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onAnimationEnd(Landroid/view/animation/Animation;)V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$1;->this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v0

    iget-boolean v0, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->isSecondEnable:Z

    if-nez v0, :cond_21

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$1;->this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->isShown()Z

    move-result v0

    if-eqz v0, :cond_21

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$1;->this$0:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->access$000(Lcom/android/systemui/newstatusbar/clock/ClockLayout;)Lcom/android/systemui/newstatusbar/clock/ClockView;

    move-result-object v1

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getText()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->onTextChanged(Ljava/lang/CharSequence;)V

    :cond_21
    return-void
.end method

.method public onAnimationRepeat(Landroid/view/animation/Animation;)V
    .registers 2

    return-void
.end method

.method public onAnimationStart(Landroid/view/animation/Animation;)V
    .registers 2

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_clock_ClockLayout_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
