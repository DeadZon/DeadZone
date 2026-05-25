"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$3.smali'
CLASS_FALLBACK_NAMES = ['ClockLayout$CenterTextView$3.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$3;
.super Ljava/lang/Object;

# interfaces
.implements Landroid/animation/ValueAnimator$AnimatorUpdateListener;


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

.field final synthetic val$height:F

.field final synthetic val$width:F


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;FF)V
    .registers 4

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$3;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    iput p2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$3;->val$width:F

    iput p3, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$3;->val$height:F

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onAnimationUpdate(Landroid/animation/ValueAnimator;)V
    .registers 9

    invoke-virtual {p1}, Landroid/animation/ValueAnimator;->getAnimatedValue()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Ljava/lang/Float;

    invoke-virtual {v0}, Ljava/lang/Float;->floatValue()F

    move-result v0

    const/high16 v1, 0x3f000000  # 0.5f

    const/4 v2, 0x0

    cmpg-float v3, v0, v2

    if-gez v3, :cond_13

    iget v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$3;->val$width:F

    :cond_13
    iget v3, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$3;->val$height:F

    mul-float/2addr v3, v1

    const/high16 v4, 0x42b40000  # 90.0f

    mul-float v5, v0, v4

    iget v6, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$3;->val$width:F

    div-float/2addr v5, v6

    iget-object v6, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$3;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    invoke-virtual {v6, v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setPivotX(F)V

    iget-object v6, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$3;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    invoke-virtual {v6, v3}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setPivotY(F)V

    invoke-static {v5}, Ljava/lang/Math;->abs(F)F

    move-result v6

    cmpl-float v6, v6, v4

    if-lez v6, :cond_37

    invoke-static {v5}, Ljava/lang/Math;->abs(F)F

    move-result v6

    div-float v6, v5, v6

    mul-float v5, v6, v4

    :cond_37
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$3;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    invoke-virtual {v4, v5}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setRotationY(F)V

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$3;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    invoke-static {v4}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->access$100(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;)F

    move-result v6

    invoke-virtual {v4, v6}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setCameraDistance(F)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_clock_ClockLayout_CenterTextView_3',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
