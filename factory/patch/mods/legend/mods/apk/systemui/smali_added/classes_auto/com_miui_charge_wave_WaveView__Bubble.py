"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/miui/charge/wave/WaveView$Bubble.smali'
CLASS_FALLBACK_NAMES = ['WaveView$Bubble.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public final Lcom/miui/charge/wave/WaveView$Bubble;
.super Ljava/lang/Object;


# instance fields
.field public Vx:F

.field public Vy:F

.field public alpha:F

.field public angle:F

.field public initAlpha:F

.field public radius:I

.field public scale:F

.field public sinRandom:F

.field public final synthetic this$0:Lcom/miui/charge/wave/WaveView;

.field public x:I

.field public y:I


# direct methods
.method public constructor <init>(Lcom/miui/charge/wave/WaveView;)V
    .registers 2

    iput-object p1, p0, Lcom/miui/charge/wave/WaveView$Bubble;->this$0:Lcom/miui/charge/wave/WaveView;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_miui_charge_wave_WaveView_Bubble',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
