"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/miui/charge/wave/WaveView$4.smali'
CLASS_FALLBACK_NAMES = ['WaveView$4.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public final Lcom/miui/charge/wave/WaveView$4;
.super Ljava/lang/Object;

# interfaces
.implements Landroid/animation/ValueAnimator$AnimatorUpdateListener;


# instance fields
.field public final synthetic this$0:Lcom/miui/charge/wave/WaveView;


# direct methods
.method public constructor <init>(Lcom/miui/charge/wave/WaveView;)V
    .registers 2

    iput-object p1, p0, Lcom/miui/charge/wave/WaveView$4;->this$0:Lcom/miui/charge/wave/WaveView;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public final onAnimationUpdate(Landroid/animation/ValueAnimator;)V
    .registers 2

    iget-object p0, p0, Lcom/miui/charge/wave/WaveView$4;->this$0:Lcom/miui/charge/wave/WaveView;

    invoke-virtual {p1}, Landroid/animation/ValueAnimator;->getAnimatedValue()Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Ljava/lang/Integer;

    invoke-virtual {p1}, Ljava/lang/Integer;->intValue()I

    move-result p1

    iput p1, p0, Lcom/miui/charge/wave/WaveView;->mWave2Dx:I

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_miui_charge_wave_WaveView_4',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
