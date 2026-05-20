"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$4.smali'
CLASS_FALLBACK_NAMES = ['ClockLayout$CenterTextView$4.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$4;
.super Landroid/animation/AnimatorListenerAdapter;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->startAnimView()V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$4;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    invoke-direct {p0}, Landroid/animation/AnimatorListenerAdapter;-><init>()V

    return-void
.end method


# virtual methods
.method public onAnimationCancel(Landroid/animation/Animator;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/animation/AnimatorListenerAdapter;->onAnimationCancel(Landroid/animation/Animator;)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$4;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->access$200(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;)V

    return-void
.end method

.method public onAnimationEnd(Landroid/animation/Animator;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/animation/AnimatorListenerAdapter;->onAnimationEnd(Landroid/animation/Animator;)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$4;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->access$200(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;)V

    return-void
.end method

.method public onAnimationPause(Landroid/animation/Animator;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/animation/AnimatorListenerAdapter;->onAnimationPause(Landroid/animation/Animator;)V

    invoke-virtual {p1}, Landroid/animation/Animator;->cancel()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$4;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->access$200(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;)V

    return-void
.end method

.method public onAnimationResume(Landroid/animation/Animator;)V
    .registers 2

    invoke-super {p0, p1}, Landroid/animation/AnimatorListenerAdapter;->onAnimationResume(Landroid/animation/Animator;)V

    invoke-virtual {p1}, Landroid/animation/Animator;->cancel()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_clock_ClockLayout_CenterTextView_4',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
