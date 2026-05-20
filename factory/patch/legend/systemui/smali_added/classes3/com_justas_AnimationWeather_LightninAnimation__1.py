"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/justas/AnimationWeather/LightninAnimation$1.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/justas/AnimationWeather/LightninAnimation$1.smali'
CLASS_FALLBACK_NAMES = ['LightninAnimation$1.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_justas_AnimationWeather_LightninAnimation$1',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/justas/AnimationWeather/LightninAnimation$1;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/justas/AnimationWeather/LightninAnimation;->startLightnin()V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/justas/AnimationWeather/LightninAnimation;\n\n\n# direct methods\n.method constructor <init>(Lcom/justas/AnimationWeather/LightninAnimation;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/justas/AnimationWeather/LightninAnimation$1;->this$0:Lcom/justas/AnimationWeather/LightninAnimation;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 2\n\n    iget-object v0, p0, Lcom/justas/AnimationWeather/LightninAnimation$1;->this$0:Lcom/justas/AnimationWeather/LightninAnimation;\n\n    invoke-virtual {v0}, Lcom/justas/AnimationWeather/LightninAnimation;->showLightnin()V\n\n    iget-object v0, p0, Lcom/justas/AnimationWeather/LightninAnimation$1;->this$0:Lcom/justas/AnimationWeather/LightninAnimation;\n\n    invoke-virtual {v0}, Lcom/justas/AnimationWeather/LightninAnimation;->startLightnin()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
