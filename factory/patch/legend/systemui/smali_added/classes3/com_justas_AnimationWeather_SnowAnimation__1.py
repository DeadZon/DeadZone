"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/justas/AnimationWeather/SnowAnimation$1.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/justas/AnimationWeather/SnowAnimation$1.smali'
CLASS_FALLBACK_NAMES = ['SnowAnimation$1.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_justas_AnimationWeather_SnowAnimation$1',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/justas/AnimationWeather/SnowAnimation$1;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/justas/AnimationWeather/SnowAnimation;->startAnimation(IIII)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/justas/AnimationWeather/SnowAnimation;\n\n.field final synthetic val$childColor:I\n\n.field final synthetic val$fallTime:I\n\n.field final synthetic val$src:I\n\n.field final synthetic val$type:I\n\n\n# direct methods\n.method constructor <init>(Lcom/justas/AnimationWeather/SnowAnimation;IIII)V\n    .registers 6\n\n    iput-object p1, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->this$0:Lcom/justas/AnimationWeather/SnowAnimation;\n\n    iput p2, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$fallTime:I\n\n    iput p3, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$src:I\n\n    iput p4, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$childColor:I\n\n    iput p5, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$type:I\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 6\n\n    iget-object v0, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->this$0:Lcom/justas/AnimationWeather/SnowAnimation;\n\n    iget v1, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$fallTime:I\n\n    iget v2, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$src:I\n\n    iget v3, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$childColor:I\n\n    iget v4, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$type:I\n\n    invoke-virtual {v0, v1, v2, v3, v4}, Lcom/justas/AnimationWeather/SnowAnimation;->startAnimation(IIII)V\n\n    iget-object v0, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->this$0:Lcom/justas/AnimationWeather/SnowAnimation;\n\n    iget v1, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$fallTime:I\n\n    iget v2, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$src:I\n\n    iget v3, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$childColor:I\n\n    iget v4, p0, Lcom/justas/AnimationWeather/SnowAnimation$1;->val$type:I\n\n    invoke-virtual {v0, v1, v2, v3, v4}, Lcom/justas/AnimationWeather/SnowAnimation;->showAnimation(IIII)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
