"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/justas/AnimationWeather/SnowAnimation$1.smali'
CLASS_FALLBACK_NAMES = ['SnowAnimation$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/justas/AnimationWeather/SnowAnimation$1;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/justas/AnimationWeather/SnowAnimation;->startAnimation(IIII)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/justas/AnimationWeather/SnowAnimation;

.field final synthetic val$childColor:I

.field final synthetic val$fallTime:I

.field final synthetic val$src:I

.field final synthetic val$type:I


# direct methods
.method constructor <init>(Lcom/justas/AnimationWeather/SnowAnimation;IIII)V
    .registers 6

    iput-object p1, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->this$0:Lcom/justas/AnimationWeather/SnowAnimation;

    iput p2, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$fallTime:I

    iput p3, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$src:I

    iput p4, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$childColor:I

    iput p5, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$type:I

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 6

    iget-object v0, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->this$0:Lcom/justas/AnimationWeather/SnowAnimation;

    iget v1, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$fallTime:I

    iget v2, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$src:I

    iget v3, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$childColor:I

    iget v4, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$type:I

    invoke-virtual {v0, v1, v2, v3, v4}, Lcom/justas/AnimationWeather/SnowAnimation;->startAnimation(IIII)V

    iget-object v0, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->this$0:Lcom/justas/AnimationWeather/SnowAnimation;

    iget v1, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$fallTime:I

    iget v2, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$src:I

    iget v3, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$childColor:I

    iget v4, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$type:I

    invoke-virtual {v0, v1, v2, v3, v4}, Lcom/justas/AnimationWeather/SnowAnimation;->showAnimation(IIII)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_justas_AnimationWeather_SnowAnimation_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
